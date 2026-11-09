PYTHON ?= python3
VENV_PYTHON := .venv/bin/python

.PHONY: all setup pdf model check clean

all: pdf

setup:
	$(PYTHON) -m venv .venv
	$(VENV_PYTHON) -m pip install -r requirements.txt

pdf:
	@test -x "$(VENV_PYTHON)" || { echo "Run make setup first." >&2; exit 1; }
	$(VENV_PYTHON) build_pdf.py

model:
	$(PYTHON) calculate_model.py

check:
	$(VENV_PYTHON) check_project.py

clean:
	rm -f paper.pdf
