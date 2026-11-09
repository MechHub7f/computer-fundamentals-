# Start here: alternate-history handoff

## What this is

An informal, explicitly labelled investment scenario with historical research behind its context. **It is not a completed factual submission for HW09.** The opening scenario notice in `paper.md` and `paper.pdf` is essential: British prices/dividends are invented; Dutch annual averages are modeled as execution-price proxies. No source verifies those invented British figures.

## Read these first

1. `paper.pdf` or `paper.md`: readable scenario and 12 linked bibliography entries.
2. `notes/research-round-1.md`: source summaries, page references, and research gaps.
3. `notes/model-and-handoff.md`: calculation assumptions, sensitivity, provenance, and next steps.
4. `data/scenario-returns.csv` and `calculate_model.py`: reproducible numerical illustration.
5. `sources/manifest.json`: citations and download URLs; `sources/download-log.json`: downloaded-file hashes.

## Reproduce on another computer

```sh
cd HW09
make setup
python3 download_sources.py
python3 extract_sources.py
make model
make check
make
```

Python 3 and a working WeasyPrint environment are required. Text extraction additionally needs Poppler's `pdftotext`. WeasyPrint may require Pango system libraries; see its installation documentation if your platform reports a missing shared library. Dependencies are installed into `.venv`, not globally. The PDF is already built locally.

Downloaded originals and extracted full-text caches are deliberately Git-ignored to avoid bloating the repository or redistributing complete copyrighted works. The manifest and scripts restore them; links remain in the bibliography. The calculated six-row scenario CSV is included as a small model output. A recipient copying only tracked project files must run the download command before recalculating it.

## Before any historical submission

- Replace the British price and dividend assumptions with verified data.
- Obtain January 1725 quotes and actual exit opportunities, not annual means used as trades.
- Verify Dutch units, chambers, payment/ex-dividend dates, and currency conversion.
- Personally read cited pages and verify translated passages against scans. AI/OCR consultation is not the student's verification.
- Search for sources refuting the resulting real-data recommendation, document the results, revise, then reread.
- Recheck bibliography classification: 6 of 12 entries contain period primary texts, some in later editions; 3 are Dutch. Consult actual passages before relying on that source count.

Git history records the handoff version. Downloaded source caches and the local virtual environment are not included in commits.
