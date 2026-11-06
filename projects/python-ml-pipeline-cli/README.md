# Python ML Pipeline CLI

A small, testable command-line data-quality utility for machine-learning pipelines. It profiles a CSV file, reports schema and missing values, and returns a stable JSON contract suitable for CI or orchestration.

## Design goals

- Small pure functions with a clear CLI boundary.
- No hidden network access or mutable global state.
- Deterministic output for automation.
- Tests that cover empty input, missing values, and invalid paths.

## Run

```bash
python -m ml_pipeline_cli --input examples/sample.csv
```
