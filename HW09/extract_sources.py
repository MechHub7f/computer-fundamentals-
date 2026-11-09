#!/usr/bin/env python3
"""Extract local sources; OCR and extracted text still require visual checking."""

from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT / "sources" / "originals"
OUTPUT = ROOT / "notes" / "extracted"


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden += 1
        if tag in {"p", "div", "li", "h1", "h2", "h3", "br", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def main():
    sources = json.loads((ROOT / "sources" / "manifest.json").read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    failures = 0
    for source in sources:
        for resource in source["files"]:
            path = ORIGINALS / resource["filename"]
            if not path.exists():
                print(f"MISSING {path.name}; run python3 download_sources.py")
                failures += 1
                continue
            output = OUTPUT / (path.stem + ".txt")
            kind = resource["format"]
            if kind == "pdf":
                if not shutil.which("pdftotext"):
                    print("MISSING pdftotext (Poppler utilities)")
                    failures += 1
                    continue
                result = subprocess.run(["pdftotext", "-layout", str(path), str(output)], check=False)
                if result.returncode:
                    failures += 1
                    continue
            elif kind == "html":
                parser = TextExtractor()
                parser.feed(path.read_text(encoding="utf-8"))
                output.write_text("".join(parser.parts), encoding="utf-8")
            elif kind == "text":
                shutil.copyfile(path, output)
            else:
                raise ValueError(f"Unsupported format: {kind}")
            print(f"EXTRACTED {output.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
