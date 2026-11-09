# HW09 — East India company investment scenario

**Start with [HANDOFF.md](HANDOFF.md).** This folder now contains an informal alternate-history paper, not a verified historical investment recommendation. Its opening notice identifies the invented British financial assumptions and the Dutch annual-average price proxies. Keep that notice with any copy.

## Main files

- `paper.md` and `paper.pdf`: readable scenario with linked bibliography.
- `HANDOFF.md`: status, reproduction commands, and historical work still required.
- `notes/research-round-1.md`: research summaries and source limitations.
- `notes/model-and-handoff.md`: modeling decisions, sensitivity, and verification priorities.
- `sources/manifest.json`: 12 sources, including six entries containing period primary texts and three Dutch entries.
- `sources/download-log.json`: downloaded-file URLs, sizes, and hashes.
- `download_sources.py` / `extract_sources.py`: source acquisition and text extraction.
- `calculate_model.py` / `data/scenario-returns.csv`: explicitly hypothetical calculation.
- `build_pdf.py`, `requirements.txt`, `Makefile`: PDF build support.
- `check_project.py`: word-count and structural checks, not historical validation.

## Build and check

On a new machine, install Python 3, then run from this directory:

```sh
make setup
make check
make
```

The PDF uses Python Markdown and WeasyPrint in a local `.venv`. No Pandoc or LaTeX is required. WeasyPrint may need operating-system Pango libraries on some machines: see [installation documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation).

To reproduce the model and extracted sources:

```sh
python3 download_sources.py
python3 extract_sources.py
make model
```

Extraction needs Poppler's `pdftotext`. Downloaded originals and full-text caches stay local and Git-ignored; scripts and links reproduce them. Do not redistribute complete works without checking rights.

## Original assignment checklist

The historical assignment asks for 1,000–1,500 words, a word count before a linked bibliography of at least 10 sources, at least half period primary and at least two non-English, notes at least twice the paper's length, and a Markdown-to-PDF build in a Git repository. Its workflow additionally requires personal reading of cited passages, a post-draft search for contrary sources, and revision.

This scenario has a body-length check, research notes, bibliography, model, and PDF. Those structural features do **not** turn invented data into historical evidence or certify completion of the required research process. See `HANDOFF.md` before formal use.

## Security

Never commit API keys or passwords. The previously shared token was not needed or added to this project; revoke it if you have not already. The downloadable source cache and local virtual environment are excluded from commits.
