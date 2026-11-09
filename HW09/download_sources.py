#!/usr/bin/env python3
"""Download the registered sources without credentials or third-party packages."""

import concurrent.futures
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "sources" / "originals"
MAX_BYTES = 100 * 1024 * 1024


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def download(item):
    source_id, resource = item
    name = resource["filename"]
    if Path(name).name != name:
        raise ValueError(f"Unsafe filename: {name}")
    target = DEST / name
    temporary = target.with_suffix(target.suffix + ".part")
    if not target.exists():
        request = urllib.request.Request(
            resource["url"],
            headers={"User-Agent": "HW09-academic-source-download/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                size = response.headers.get("Content-Length")
                if size and int(size) > MAX_BYTES:
                    raise ValueError(f"Source exceeds {MAX_BYTES} bytes")
                total = 0
                with temporary.open("wb") as output:
                    while True:
                        chunk = response.read(1024 * 1024)
                        if not chunk:
                            break
                        total += len(chunk)
                        if total > MAX_BYTES:
                            raise ValueError("Download exceeded size limit")
                        output.write(chunk)
            if not temporary.stat().st_size:
                raise ValueError("Empty download")
            if resource["format"] == "pdf":
                with temporary.open("rb") as stream:
                    if not stream.read(1024).lstrip().startswith(b"%PDF-"):
                        raise ValueError("Expected PDF; server returned other content")
            temporary.replace(target)
        finally:
            temporary.unlink(missing_ok=True)
    return {
        "source_id": source_id,
        "filename": name,
        "url": resource["url"],
        "bytes": target.stat().st_size,
        "sha256": digest(target),
    }


def main():
    sources = json.loads((ROOT / "sources" / "manifest.json").read_text())
    DEST.mkdir(parents=True, exist_ok=True)
    work = [(source["id"], item) for source in sources for item in source["files"]]
    records, failures = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(download, item): item for item in work}
        for future in concurrent.futures.as_completed(futures):
            source_id, item = futures[future]
            try:
                record = future.result()
                records.append(record)
                print(f"OK {record['filename']} ({record['bytes']:,} bytes)")
            except Exception as error:
                failures.append({"source_id": source_id, "filename": item["filename"], "error": str(error)})
                print(f"FAILED {item['filename']}: {error}", file=sys.stderr)
    report = {"files": sorted(records, key=lambda record: record["filename"]), "failures": failures}
    (ROOT / "sources" / "download-log.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
