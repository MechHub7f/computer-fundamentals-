#!/usr/bin/env python3
"""Render the complete paper, including its scenario notice, as a PDF."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def main():
    try:
        import markdown
        from weasyprint import HTML, CSS
    except ImportError:
        sys.exit("Missing PDF dependencies. Run make setup first.")
    text = (ROOT / "paper.md").read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>An Ancestor’s Investment</title></head><body>' + body + '</body></html>'
    css = CSS(string="""
        @page { size: letter; margin: .8in .85in;
            @bottom-center { content: counter(page); font-size: 9pt; } }
        body { font-family: 'DejaVu Serif', serif; font-size: 10.5pt; line-height: 1.45; }
        h1 { font-size: 20pt; line-height: 1.2; }
        h2 { font-size: 14pt; margin-top: 1.3em; }
        h3 { font-size: 11pt; }
        h1, h2, h3 { break-after: avoid; }
        p { orphans: 3; widows: 3; }
        blockquote { margin: 1em 0; padding: .65em 1em; background: #f1f3f5;
            border-left: 3px solid #475569; font-size: 9pt; }
        table { width: 100%; border-collapse: collapse; font-size: 9.5pt; }
        td, th { border-bottom: 1px solid #ccc; padding: .4em; }
        tr { break-inside: avoid; }
        a { color: #164e79; overflow-wrap: anywhere; }
        li { margin-bottom: .6em; }
    """)
    HTML(string=html, base_url=str(ROOT)).write_pdf(ROOT / "paper.pdf", stylesheets=[css])
    print("Built", ROOT / "paper.pdf")


if __name__ == "__main__":
    main()
