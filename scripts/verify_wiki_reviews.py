#!/usr/bin/env python3
"""P1 human-attested Wiki review gate + automated evidence warning inventory.

All published articles begin pending; passing this check DOES NOT mean
expert-reviewed. A verified review needs a human handle, date, content hash,
specific claim/evidence pairs and a checked-example attestation.
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

ROOT=Path(__file__).resolve().parents[1]
LEDGER=Path("wiki/reviews/ai-infrastructure.json")
INDEX=Path("docs/data/wiki-index.json")
HEADINGS=("核心定义","形象理解","技术原理","工程实践","面试题","考试题")
GENERIC=("官方技术资料","原始规范、维护者文档或公开技术说明","请核对所用硬件与文档版本")
DATE=re.compile(r"^\d{4}-\d{2}-\d{2}$")
HANDLE=re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
SHA=re.compile(r"^[a-f0-9]{64}$")
def valid_url(text):
    u=urlparse(str(text))
    return u.scheme=="https" and bool(u.netloc) and not u.username and not u.password

def audit(root=ROOT):
    errors=[];warnings=[]
    try:
        index=json.loads((root/INDEX).read_text(encoding="utf-8"))
        ledger=json.loads((root/LEDGER).read_text(encoding="utf-8"))
        expected={a["path"] for a in index["articles"]}
        records=ledger["articles"]
        if ledger["schemaVersion"]!=1 or ledger["domain"]!="ai-infrastructure":
            errors.append("Unsupported review ledger schema/domain")
        paths=[r["path"] for r in records]
        if set(paths)!=expected or len(paths)!=len(expected):
            errors.append("Review ledger must cover every published article exactly once")
        approved=0
        for record in records:
            path=record.get("path","")
            if path not in expected:continue
            article=(root/path)
            if not article.is_file():
                errors.append(f"{path}: missing Markdown")
                continue
            content=article.read_text(encoding="utf-8")
            digest=hashlib.sha256(article.read_bytes()).hexdigest()
            links=re.findall(r"\[[^\]]+\]\((https?://[^)\s]+)\)",content)
            if not links: errors.append(f"{path}: no actionable reference URL")
            for heading in HEADINGS:
                if heading not in content: errors.append(f"{path}: missing section {heading}")
            for indicator in GENERIC:
                if indicator in content: warnings.append(f"{path}: generic reference language ({indicator})")
            if len(links)<2:
                warnings.append(f"{path}: fewer than two independently linked references")
            status=record.get("status")
            if status=="pending":
                if any(record.get(k) for k in ("reviewer","reviewed_at","sha256","attestations")):
                    errors.append(f"{path}: pending review cannot impersonate an attested review")
                warnings.append(f"{path}: independent technical review still pending")
            elif status=="verified":
                approved+=1
                if not HANDLE.fullmatch(str(record.get("reviewer",""))):
                    errors.append(f"{path}: missing human reviewer GitHub handle")
                day=record.get("reviewed_at","")
                if not DATE.fullmatch(str(day)):
                    errors.append(f"{path}: invalid review date")
                else:
                    try:
                        when=date.fromisoformat(day)
                        if when>date.today():errors.append(f"{path}: review date in future")
                    except ValueError: errors.append(f"{path}: impossible review date")
                if not SHA.fullmatch(str(record.get("sha256",""))) or record.get("sha256")!=digest:
                    errors.append(f"{path}: edited content invalidates human sign-off")
                a=record.get("attestations",{})
                if not isinstance(a,dict):a={}
                if not all(a.get(k) is True for k in ("definitions","mechanisms","examples","interview_answers","exam_answers","version_scope","copyright")):
                    errors.append(f"{path}: signed review lacks required factual attestations")
                claims=record.get("claims",[])
                if not isinstance(claims,list) or len(claims)<2:
                    errors.append(f"{path}: human review requires two specific claim/evidence mappings")
                else:
                    for item in claims:
                        if not all(isinstance(item.get(k),str) and len(item[k].strip())>5 for k in ("claim","locator","rationale")) or not valid_url(item.get("url")):
                            errors.append(f"{path}: invalid source/claim/locator evidence")
            else:errors.append(f"{path}: invalid review status {status!r}")
        return errors,warnings,approved,len(expected)
    except (OSError,KeyError,ValueError,TypeError) as e:
        return [f"Unable to load review ledger: {e}"],[],0,0

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check",action="store_true")
    p.add_argument("--report",action="store_true")
    args=p.parse_args()
    errors,warnings,verified,total=audit()
    if args.report:
        Path("wiki-evidence-report.json").write_text(json.dumps({
          "schemaVersion":1,"total":total,"humanVerified":verified,"humanPending":total-verified,
          "blockingErrors":errors,"reviewWarnings":warnings,
          "scope":"Offline structural/source-label audit only, not external claim verification"
        },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for item in errors:print("ERROR:",item)
    for item in warnings[:25]:print("REVIEW:",item)
    if len(warnings)>25:print("REVIEW:",len(warnings)-25,"additional findings in report")
    print(f"WIKI REVIEW: {verified}/{total} human-attested; {total-verified} pending; {len(errors)} blocking errors; {len(warnings)} editorial warnings")
    return 1 if errors else 0
if __name__=="__main__":sys.exit(main())
