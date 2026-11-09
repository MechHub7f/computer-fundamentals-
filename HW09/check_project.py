#!/usr/bin/env python3
"""Structural checks only; passing does NOT certify historical accuracy."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import markdown

ROOT = Path(__file__).resolve().parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, value):
        self.parts.append(value)


def count(value):
    parser = Text()
    parser.feed(markdown.markdown(value, extensions=['tables']))
    return len(' '.join(parser.parts).split())


def body(text):
    return text.split('## The decision', 1)[1].split('**Word count:**', 1)[0]


if __name__ == '__main__':
    text = (ROOT / 'paper.md').read_text()
    words = count(body(text))
    notes = sum(count((ROOT / name).read_text()) for name in ['notes/research-round-1.md', 'notes/model-and-handoff.md'])
    claimed = int(re.search(r'\*\*Word count:\*\* (\d+)', text).group(1))
    manifest = json.loads((ROOT / 'sources/manifest.json').read_text())
    cited = set(re.findall(r'\*\*\[([PSD]\d+)\]\*\*', text))
    primary = {s['id'] for s in manifest if s['id'].startswith('P')}
    assert 1000 <= words <= 1500, words
    assert claimed == words, (claimed, words)
    assert notes >= 2 * words, (notes, words)
    assert len(cited) >= 10 and len(cited & primary) * 2 >= len(cited)
    assert len([s for s in manifest if s['id'] in cited and s['language'] == 'Dutch']) >= 2
    assert '**Scenario notice:**' in text and 'invented modeling assumptions' in text
    print(f'Paper body: {words} words; substantive notes: {notes} words.')
    print(f'Bibliography: {len(cited)} entries; {len(cited & primary)} period-primary text entries.')
    print('Structural checks passed. Historical verification and assignment completion are NOT certified.')
