#!/usr/bin/env python3
"""Render the authored Operating Systems handbook PDF from its printable HTML."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/source/operating-systems.html"
DEST = ROOT / "pdf/operating-systems.pdf"
PAGES = ROOT / "docs/pdf/operating-systems.pdf"


def main():
    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise SystemExit("Install WeasyPrint: python3 -m pip install weasyprint==68.0") from exc
    if not SOURCE.is_file():
        raise SystemExit(f"Missing OS printable HTML source: {SOURCE}")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    PAGES.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(SOURCE), base_url=str(ROOT)).write_pdf(str(DEST))
    if DEST.stat().st_size < 10_000 or DEST.read_bytes()[:5] != b"%PDF-":
        raise SystemExit("Rendered OS PDF is missing or invalid")
    shutil.copy2(DEST, PAGES)
    print(f"Operating Systems PDF generated: {DEST} ({DEST.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
