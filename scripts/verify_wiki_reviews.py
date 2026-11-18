#!/usr/bin/env python3
"""Audit published Wiki articles against per-domain expert review ledgers.

Pending is an honest unreviewed state; this script only checks consistency and
source-link presence. It NEVER certifies the correctness of technical claims.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = Path("docs/data/wiki-index.json")
REVIEW_DIR = Path("wiki/reviews")
HEADINGS = ("核心定义", "形象理解", "技术原理", "工程实践", "面试题", "考试题")
GENERIC = ("官方技术资料", "原始规范、维护者文档或公开技术说明", "请核对所用硬件与文档版本")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HANDLE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
SHA = re.compile(r"^[a-f0-9]{64}$")

def valid_url(value):
    parsed = urlparse(str(value))
    return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username and not parsed.password

def audit(root=ROOT):
    errors, warnings = [], []
    try:
        index = json.loads((root / INDEX).read_text(encoding="utf-8"))
        expected = {entry["path"] for entry in index["articles"]}
        if len(expected) != len(index["articles"]):
            errors.append("Duplicate paths in public Wiki index")
        by_domain = {}
        for path in expected:
            parts = Path(path).parts
            if len(parts) != 3 or parts[0] != "wiki":
                errors.append(f"Invalid Wiki article path: {path}")
                continue
            by_domain.setdefault(parts[1], set()).add(path)
        covered = set()
        approved = 0
        for domain, paths in sorted(by_domain.items()):
            ledger_path = root / REVIEW_DIR / f"{domain}.json"
            if not ledger_path.is_file():
                errors.append(f"Missing review ledger for {domain}")
                continue
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
            if ledger.get("schemaVersion") != 1 or ledger.get("domain") != domain:
                errors.append(f"Unsupported review ledger schema/domain: {domain}")
            records = ledger.get("articles", [])
            if not isinstance(records, list):
                errors.append(f"{domain}: articles must be a list")
                continue
            actual_paths = [r.get("path") for r in records]
            if len(set(actual_paths)) != len(actual_paths) or set(actual_paths) != paths:
                errors.append(f"{domain}: review ledger must cover every published article exactly once")
            for record in records:
                path = record.get("path", "")
                if path not in paths:
                    continue
                covered.add(path)
                source = root / path
                if not source.is_file():
                    errors.append(f"{path}: missing Markdown")
                    continue
                body = source.read_bytes()
                content = body.decode("utf-8")
                digest = hashlib.sha256(body).hexdigest()
                links = re.findall(r"\[[^\]]+\]\((https?://[^)\s]+)\)", content)
                if not links:
                    errors.append(f"{path}: no actionable reference URL")
                elif len(links) < 2:
                    warnings.append(f"{path}: fewer than two independently linked references")
                for heading in HEADINGS:
                    if heading not in content:
                        errors.append(f"{path}: missing section {heading}")
                for indicator in GENERIC:
                    if indicator in content:
                        warnings.append(f"{path}: generic reference language ({indicator})")
                status = record.get("status")
                if status == "pending":
                    if any(record.get(k) for k in ("reviewer", "reviewed_at", "sha256", "attestations", "claims")):
                        errors.append(f"{path}: pending review cannot impersonate an attested review")
                    warnings.append(f"{path}: independent technical review still pending")
                elif status == "verified":
                    approved += 1
                    if not HANDLE.fullmatch(str(record.get("reviewer", ""))):
                        errors.append(f"{path}: missing human reviewer GitHub handle")
                    reviewed = record.get("reviewed_at", "")
                    if not DATE.fullmatch(str(reviewed)):
                        errors.append(f"{path}: invalid review date")
                    else:
                        try:
                            if date.fromisoformat(reviewed) > date.today():
                                errors.append(f"{path}: review date in future")
                        except ValueError:
                            errors.append(f"{path}: impossible review date")
                    if not SHA.fullmatch(str(record.get("sha256", ""))) or record.get("sha256") != digest:
                        errors.append(f"{path}: edited content invalidates human sign-off")
                    attest = record.get("attestations", {})
                    if not isinstance(attest, dict):
                        attest = {}
                    needed = ("definitions", "mechanisms", "examples", "interview_answers", "exam_answers", "version_scope", "copyright")
                    if not all(attest.get(key) is True for key in needed):
                        errors.append(f"{path}: signed review lacks required factual attestations")
                    claims = record.get("claims", [])
                    if not isinstance(claims, list) or len(claims) < 2:
                        errors.append(f"{path}: human review requires two specific claim/evidence mappings")
                    else:
                        for item in claims:
                            if not isinstance(item, dict) or not all(isinstance(item.get(k), str) and len(item[k].strip()) > 5 for k in ("claim","locator","rationale")) or not valid_url(item.get("url")):
                                errors.append(f"{path}: invalid source/claim/locator evidence")
                else:
                    errors.append(f"{path}: invalid review status {status!r}")
        if covered != expected:
            errors.append(f"Review ledger coverage mismatch: missing {len(expected-covered)}, extra {len(covered-expected)}")
        for file in (root / REVIEW_DIR).glob("*.json"):
            if file.stem not in by_domain:
                errors.append(f"Orphan review ledger not linked to public Wiki: {file.name}")
        return errors, warnings, approved, len(expected)
    except (OSError, KeyError, ValueError, TypeError, UnicodeError) as exc:
        return [f"Unable to load review ledger: {exc}"], [], 0, 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    errors, warnings, verified, total = audit()
    if args.report:
        Path("wiki-evidence-report.json").write_text(json.dumps({
            "schemaVersion": 1, "total": total, "humanVerified": verified,
            "humanPending": total-verified, "blockingErrors": errors,
            "reviewWarnings": warnings,
            "scope": "Offline structural/source-label audit only, not external claim verification"
        }, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    for item in errors:
        print("ERROR:", item)
    for item in warnings[:25]:
        print("REVIEW:", item)
    if len(warnings) > 25:
        print("REVIEW:", len(warnings)-25, "additional findings in report")
    print(f"WIKI REVIEW: {verified}/{total} human-attested; {total-verified} pending; {len(errors)} blocking errors; {len(warnings)} editorial warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
