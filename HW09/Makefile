PYTHON ?= python3
VENV_PYTHON := .venv/bin/python

# On a new machine, run `make setup` once, then run `make`.
.PHONY: all setup pdf clean

all: pdf

setup:
	$(PYTHON) -m venv .venv
	$(VENV_PYTHON) -m pip install -r requirements.txt

pdf:
	@test -x "$(VENV_PYTHON)" || { echo "Run make setup first." >&2; exit 1; }
	$(VENV_PYTHON) build_pdf.py

clean:
	rm -f paper.pdf
