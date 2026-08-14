#!/usr/bin/env python3
"""Fetch literature metadata + abstract by PMID or DOI.

Prefer PubMed / NCBI E-utilities. Fall back to Crossref for DOI metadata
when PubMed resolution fails. Stdlib only. Prints one JSON object to stdout.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any

NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
CROSSREF_BASE = "https://api.crossref.org/works"
TOOL = "malt-med-evidence"
DEFAULT_EMAIL = "malt-med-evidence@local.invalid"
USER_AGENT = f"{TOOL}/1.0 (stdlib; educational literature fetch)"


def _email() -> str:
    return os.environ.get("NCBI_EMAIL", DEFAULT_EMAIL).strip() or DEFAULT_EMAIL


def _http_get(url: str, timeout: float = 30.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _ncbi_params(**extra: str) -> str:
    params = {"tool": TOOL, "email": _email(), **extra}
    return urllib.parse.urlencode(params)


def normalize_doi(raw: str) -> str:
    s = raw.strip()
    s = re.sub(r"^https?://(dx\.)?doi\.org/", "", s, flags=re.I)
    s = re.sub(r"^doi:\s*", "", s, flags=re.I)
    return s.strip()


def normalize_pmid(raw: str) -> str:
    s = raw.strip()
    s = re.sub(r"^PMID[:\s]*", "", s, flags=re.I)
    if not re.fullmatch(r"\d+", s):
        raise ValueError(f"Invalid PMID: {raw!r}")
    return s


def pmid_from_doi(doi: str) -> str | None:
    q = _ncbi_params(db="pubmed", term=f"{doi}[DOI]", retmax="1")
    url = f"{NCBI_BASE}/esearch.fcgi?{q}"
    data = _http_get(url)
    root = ET.fromstring(data)
    ids = [el.text for el in root.findall(".//IdList/Id") if el.text]
    return ids[0] if ids else None


def _text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return "".join(el.itertext()).strip()


def fetch_pubmed(pmid: str) -> dict[str, Any]:
    q = _ncbi_params(db="pubmed", id=pmid, retmode="xml")
    url = f"{NCBI_BASE}/efetch.fcgi?{q}"
    root = ET.fromstring(_http_get(url))
    article = root.find(".//PubmedArticle")
    if article is None:
        raise LookupError(f"PMID {pmid} not found in PubMed")

    medline = article.find(".//MedlineCitation")
    art = medline.find("Article") if medline is not None else None
    if art is None:
        raise LookupError(f"Incomplete PubMed record for PMID {pmid}")

    title = _text(art.find("ArticleTitle"))
    abstract_bits = [_text(n) for n in art.findall(".//Abstract/AbstractText")]
    abstract = "\n".join(b for b in abstract_bits if b)

    authors: list[str] = []
    for a in art.findall(".//AuthorList/Author"):
        last = _text(a.find("LastName"))
        initials = _text(a.find("Initials"))
        collective = _text(a.find("CollectiveName"))
        if collective:
            authors.append(collective)
        elif last:
            authors.append(f"{last} {initials}".strip())

    journal = _text(art.find(".//Journal/Title")) or _text(
        art.find(".//Journal/ISOAbbreviation")
    )
    year = ""
    for path in (
        ".//Journal/JournalIssue/PubDate/Year",
        ".//ArticleDate/Year",
        ".//PubmedData/History/PubMedPubDate/Year",
    ):
        y = _text(article.find(path))
        if y:
            year = y
            break
    if not year:
        medline_date = _text(art.find(".//Journal/JournalIssue/PubDate/MedlineDate"))
        m = re.search(r"\d{4}", medline_date or "")
        if m:
            year = m.group(0)

    pub_types = [_text(n) for n in art.findall(".//PublicationTypeList/PublicationType")]
    pub_types = [p for p in pub_types if p]

    doi = ""
    for aid in article.findall(".//ArticleIdList/ArticleId"):
        if aid.attrib.get("IdType") == "doi" and aid.text:
            doi = aid.text.strip()
            break

    return {
        "id": pmid,
        "id_type": "pmid",
        "pmid": pmid,
        "doi": doi,
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "journal": journal,
        "year": year,
        "publication_types": pub_types,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "source": "pubmed",
        "abstract_available": bool(abstract),
        "warnings": [] if abstract else ["No abstract in PubMed record"],
    }


def fetch_crossref(doi: str) -> dict[str, Any]:
    url = f"{CROSSREF_BASE}/{urllib.parse.quote(doi)}"
    payload = json.loads(_http_get(url).decode("utf-8"))
    msg = payload.get("message") or {}
    title_list = msg.get("title") or []
    title = title_list[0] if title_list else ""

    authors: list[str] = []
    for a in msg.get("author") or []:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        name = f"{family} {given}".strip() if family or given else (a.get("name") or "").strip()
        if name:
            authors.append(name)

    year = ""
    for key in ("published-print", "published-online", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0]:
            year = str(parts[0][0])
            break

    journal_list = msg.get("container-title") or []
    journal = journal_list[0] if journal_list else ""
    pub_types = [msg.get("type")] if msg.get("type") else []
    abstract = msg.get("abstract") or ""
    if abstract:
        # Crossref abstracts are sometimes JATS XML snippets.
        abstract = re.sub(r"<[^>]+>", " ", abstract)
        abstract = re.sub(r"\s+", " ", abstract).strip()

    warnings = [
        "Resolved via Crossref metadata fallback (not PubMed)",
    ]
    if not abstract:
        warnings.append("No abstract from Crossref; request abstract/methods from user")

    return {
        "id": doi,
        "id_type": "doi",
        "pmid": None,
        "doi": doi,
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "journal": journal,
        "year": year,
        "publication_types": pub_types,
        "url": f"https://doi.org/{doi}",
        "source": "crossref",
        "abstract_available": bool(abstract),
        "warnings": warnings,
    }


def fetch(pmid: str | None = None, doi: str | None = None) -> dict[str, Any]:
    if bool(pmid) == bool(doi):
        raise ValueError("Provide exactly one of --pmid or --doi")

    if pmid:
        return fetch_pubmed(normalize_pmid(pmid))

    doi_n = normalize_doi(doi or "")
    if not doi_n:
        raise ValueError("Empty DOI")

    # Prefer PubMed when indexed.
    time.sleep(0.34)  # be polite to NCBI (~3 rps without API key)
    try:
        found = pmid_from_doi(doi_n)
    except Exception as exc:  # noqa: BLE001 — report and fall back
        found = None
        pubmed_err = str(exc)
    else:
        pubmed_err = None

    if found:
        time.sleep(0.34)
        rec = fetch_pubmed(found)
        rec["doi"] = rec.get("doi") or doi_n
        rec["query_doi"] = doi_n
        return rec

    time.sleep(0.2)
    rec = fetch_crossref(doi_n)
    if pubmed_err:
        rec["warnings"].append(f"PubMed lookup failed before Crossref fallback: {pubmed_err}")
    else:
        rec["warnings"].append("DOI not found in PubMed; used Crossref fallback")
    return rec


def detect_token(token: str) -> tuple[str, str]:
    t = token.strip()
    if re.fullmatch(r"\d+", t) or re.match(r"^PMID[:\s]*\d+$", t, re.I):
        return "pmid", normalize_pmid(t)
    if "doi.org/" in t.lower() or t.lower().startswith("doi:") or "/" in t:
        return "doi", normalize_doi(t)
    raise ValueError(f"Cannot detect PMID or DOI from token: {token!r}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pmid", help="PubMed ID")
    parser.add_argument("--doi", help="DOI")
    parser.add_argument(
        "token",
        nargs="?",
        help="Optional bare PMID or DOI (also accepted on stdin if no args)",
    )
    args = parser.parse_args(argv)

    pmid = args.pmid
    doi = args.doi
    token = args.token

    if not pmid and not doi and not token and not sys.stdin.isatty():
        token = sys.stdin.read().strip()

    try:
        if token and not pmid and not doi:
            kind, value = detect_token(token)
            if kind == "pmid":
                pmid = value
            else:
                doi = value
        result = fetch(pmid=pmid, doi=doi)
    except (ValueError, LookupError, urllib.error.URLError, ET.ParseError, json.JSONDecodeError) as exc:
        err = {
            "ok": False,
            "error": str(exc),
            "pmid": pmid,
            "doi": doi,
        }
        print(json.dumps(err, ensure_ascii=False, indent=2))
        return 1

    result["ok"] = True
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
