"""Reproducibly normalize the two repository-owned snapshots, without network data."""
import csv
import json
import math
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]

def number(value):
    text = str(value).strip().replace('−', '-').replace(',', '').replace('$', '').replace('%', '')
    try:
        result = float(text)
        return result if math.isfinite(result) else None
    except ValueError:
        return None

def write(data):
    (ROOT/'data.js').write_text('window.DATA = '+json.dumps(data,ensure_ascii=False,separators=(',', ':'))+';\n',encoding='utf-8')

aqi = ROOT

source = aqi / '1. Exploratory Data Analysis (EDA) project/data/raw/delhi_air_quality_clean.csv'
with source.open(encoding='utf-8-sig', newline='') as stream:
    rows = [dict(date=date(int(r['Year']), int(r['Month']), int(r['Date'])).isoformat(), **{k:number(r[k]) for k in ['AQI', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone']}) for r in csv.DictReader(stream)]
rows.sort(key=lambda r:r['date'])
write(rows)
