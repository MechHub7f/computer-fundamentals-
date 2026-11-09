#!/usr/bin/env python3
"""Reproduce an alternate-history model, NOT a historical EIC backtest."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# These British inputs are invented for the explicitly labelled scenario.
EIC_PURCHASE = 150.0
EIC_ANNUAL_DIVIDEND = 8.0
EIC_EXITS = {1745: 170.0, 1746: 160.0, 1747: 165.0, 1748: 180.0, 1749: 190.0, 1750: 200.0}


def results():
    source = ROOT / 'sources/originals/D01-voc-dividends.tsv'
    if not source.exists():
        raise SystemExit('Run python3 download_sources.py to retrieve the VOC dataset first.')
    with source.open(encoding='utf-8') as stream:
        rows = {int(r['Year']): r for r in csv.DictReader(stream, delimiter='\t')}
    # Annual averages are hypothetical execution-price proxies, not dated quotes.
    purchase = float(rows[1725]['avstockcourseVOCAMS'])
    dividends = 0.0
    output = []
    for year in range(1726, 1751):
        # Interpret DivPct as the fraction of nominal capital paid each year.
        dividends += 100 * float(rows[year]['DivPct'])
        if year not in EIC_EXITS:
            continue
        british_dividends = (year - 1725) * EIC_ANNUAL_DIVIDEND
        exit_price = float(rows[year]['avstockcourseVOCAMS'])
        output.append({
            'exit_year': year,
            'eic_input_kind': 'invented_scenario',
            'eic_purchase': EIC_PURCHASE,
            'eic_exit': EIC_EXITS[year],
            'eic_cumulative_dividends': british_dividends,
            'eic_return_pct': 100 * (EIC_EXITS[year] + british_dividends - EIC_PURCHASE) / EIC_PURCHASE,
            'voc_input_kind': 'annual_average_proxy_not_execution_quote',
            'voc_purchase_proxy': purchase,
            'voc_exit_proxy': exit_price,
            'voc_cumulative_dividends_assumed_nominal': dividends,
            'voc_proxy_return_pct': 100 * (exit_price + dividends - purchase) / purchase,
        })
    return output


if __name__ == '__main__':
    output = results()
    dest = ROOT / 'data/scenario-returns.csv'
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(output[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(output)
    for row in output:
        print(f"{row['exit_year']}: EIC scenario {row['eic_return_pct']:.1f}%; VOC proxy {row['voc_proxy_return_pct']:.1f}%")
    print('Wrote', dest)
