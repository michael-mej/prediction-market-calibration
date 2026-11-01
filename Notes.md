# Notes

## Phase 1 — Polymarket API exploration (Sept 2026, abandoned)

Abandoned because Polymarket is not accessible from Quebec, so no live forecasting is possible on it. Kept for the findings about the Gamma API, which are not documented anywhere else.

### Session 1

Got in touch with the Polymarket Gamma API and downloaded one resolved market into a JSON file (in `data`). The fetching program in `src` was written to extract a single already-resolved market.

### Session 2

Requested more markets from the API. Established that the maximum limit it returns at a time is 100. Pulled the data into CSV and into a pandas DataFrame.

Findings:

- Many columns are mostly null (rows 72 to 89, with the exception of 73 and 82).
- There is no explicit winner field. Resolution is encoded in `outcomePrices`.
- `outcomes` and `outcomePrices` are returned as JSON-encoded strings, not lists, which breaks `mode()`, `nunique()` and `value_counts()` at DataFrame level with `TypeError: unhashable type: 'list'`.
- A resolved market gives `outcomePrices` of the form `[number near 1, number near 0]`. But most closed markets return `[0, 0]`, and some return values near 0.5, meaning the final share price was neither 1 nor 0.

Open question at the point of abandonment: which column separates the `[0, 0]` rows from properly resolved ones. That column would have been the real resolution flag and the exclusion rule for the dataset.

## Phase 2 — ForecastEx forecast journal (Nov 2026)

Current phase. See README for scope.
