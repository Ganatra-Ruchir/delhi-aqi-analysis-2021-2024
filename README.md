# Atmos — Delhi Historical Air Quality Explorer V2

An interactive research workspace over the repository's 1,461 daily observations from 2021-01-01 through 2024-12-31. Filter dates, inspect pollutants, compare periods, analyze thresholds and export evidence.

## Start

```sh
python -m http.server 8000
```

Open http://localhost:8000. The default `index.html` is the V2 explorer. The earlier narrative is retained at [story.html](story.html). No account, API key, build step or external chart service is required.

## Features and validation

See [the V2 feature ledger](V2_RELEASE.md) for 15 capabilities and operating limits.

```sh
node --test tests/*.test.cjs
npm ci
npx playwright install chromium
npm run test:browser
```

## Data and reproducibility

Original CSV: `1. Exploratory Data Analysis (EDA) project/data/raw/delhi_air_quality_clean.csv`.
Existing notebooks and Streamlit source are retained in that project folder.

`python scripts/build_data.py` regenerates the browser snapshot `data.js` from the original CSV, preserving missing values and sorting ISO dates. The browser calculates all new explorer statistics from this snapshot.

Upstream station coverage, revision history and pollutant concentration units are not fully documented in this repository. Pollutants are therefore labelled **source units**. This is historical descriptive analysis, not a live reading, medical recommendation, causal model or forecast. A season's mean should not be interpreted as the category of every day in that season.

The explorer includes missing-value, duplicate-date and calendar-coverage counts. New analysis should be backed by the exported slice, not by claims copied from earlier project notes.
