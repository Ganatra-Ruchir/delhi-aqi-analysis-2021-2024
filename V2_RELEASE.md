# Atmos — Historical AQI Explorer V2

Release date: 12 October 2026.

## User-facing features

1. Filter observations by inclusive start/end date.
2. Explore AQI or six individual pollutants.
3. Overlay a trailing 7- or 30-observation average.
4. Calculate the selected range’s mean, median and maximum.
5. Adjust an AQI threshold and count exceedance days.
6. Measure the longest consecutive-day exceedance run.
7. Inspect AQI category counts at documented boundaries.
8. Compare calendar-month means.
9. Compare years with explicit observation counts.
10. Inspect a paginated daily ledger sorted by value or date.
11. Export the complete filtered range as CSV.
12. Download a research summary with current parameters.
13. Share filters in a URL.
14. Inspect missing cells, duplicate dates and calendar coverage.
15. Switch and remember light/dark theme.

## Use and limits

Run `python -m http.server 8000` and open index.html. The previous narrative is preserved at story.html; notebooks and original CSVs remain in their existing folder. Data spans 2021–2024, not current conditions. Pollutant units, station coverage and upstream methodology are not fully documented; values are labelled source units. Results are descriptive, not causal, clinical or predictive. Category cutoffs are the convention used by this dataset.

## Interface and reliability

Responsive layouts, keyboard focus, lightweight CSS animation with a pause control, and operating-system reduced-motion support. CSV exports quote values and neutralize common spreadsheet formula prefixes. Browser checks cover representative workflows, download events, reload persistence where applicable, JavaScript errors and mobile overflow. Passing these checks is not a guarantee of zero defects.

## Verification

```sh
npm ci
npx playwright install chromium
npm run test:browser
```

