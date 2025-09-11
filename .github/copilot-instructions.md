## Quick orientation for AI coding agents

Goal: help an agent be productive in this repo by describing the architecture, data flows, developer commands, and code conventions that are discoverable from the code.

1) Big-picture architecture
- Single small visualization app using marimo cells in `app_beta.py` as the UI/driver.
- Data layer: `scratch.py` provides polars-based lazy loaders and filter helpers that operate on a single Parquet source (path in `config.py` as `BASE_DATA`).
- Presentation: `figures.py` builds Plotly charts from collected frames. The app glue calls `filter_map_data` and `filter_line_data` (both return polars LazyFrames) then collects results for the Plotly functions.

2) Data flow and important functions (concrete)
- `config.py` -> `BASE_DATA` is an absolute Path to a Parquet file. Agents must not assume test data exists; verify the path before running.
- `scratch.load_base_data()` returns a `pl.LazyFrame` via `pl.scan_parquet(BASE_DATA)`.
- Filtering helpers used by the UI:
  - `filter_map_data(year_quarter, drug, brand_generic, utilization_type)` -> LazyFrame grouped by `state` and computes aggregated totals and expressions `payment_per_unit` and `markup_per_unit`.
  - `filter_line_data(state, drug, brand_generic, utilization_type)` -> LazyFrame grouped by a constructed `date` (quarter -> month) and returns `payment_per_unit`, `weighted_nadac_per_unit`, `markup_per_unit`.
- Expression helpers return `pl.Expr` objects (e.g. `payment_per_unit()`, `weighted_nadac_per_unit()`) and are used inside `.with_columns(...)`.

3) Running / developer workflows (commands validated by files)
- Recommended environment: Python venv in `.venv` (project shows activation in a terminal). On Windows using bash:

```bash
source .venv/Scripts/activate
python app_beta.py
```

- Requirements found in `requirements.txt`: `polars`, `plotly`, `pandas`, `pyarrow`. Install with `pip install -r requirements.txt` inside the venv.

4) Project-specific conventions and gotchas
- Most data functions return `pl.LazyFrame` (not eager DataFrames). Callers in `app_beta.py` typically call `.collect()` (sometimes with streaming engine) before passing to Plotly.
- Dropdown helper functions return plain Python lists (e.g. `drug_list()`, `state_list()`, `year_quarter_list()`) used by the marimo UI.
- `brand_generic` values expected by the code are literal strings like `'Brand'` and `'Generic'` (case-sensitive in the branch checks inside `scratch.py`).
- `utilization_type` uses 'ffsu' vs 'mcou' booleans via column predicates `c.is_ffsu`.
- `collect(engine='streaming')` is used in several places — keep streaming-compatible transforms when possible.

5) Integration points & external dependencies
- Data file: `BASE_DATA` (Parquet) is the single external data dependency. Agents modifying data-loading must update `config.py` or accept a param override.
- UI framework: `marimo` (app defined in `app_beta.py`) — inspect cells to see how values flow from UI widgets into filter helpers.
- Charting: Plotly in `figures.py`; the heat-map converts polars frames to pandas via `.to_pandas()`.

6) Where to make common changes (examples)
- Add a new metric: implement a new `pl.Expr` helper in `scratch.py` (pattern: return pl expression, alias it) and add it into the `.with_columns(...)` or `.agg(...)` where appropriate. Update `figures.py` to use the metric name for color/lines.
- Change data source: update `config.py` BASE_DATA Path. Prefer making path configurable via an environment variable if adding tests.

7) Minimal checklist for safe edits by an agent
- Ensure LazyFrame vs collected DataFrame expectations are preserved.
- Preserve string literal conventions for dropdown filters (`'Brand'`/`'Generic'`, `'ffsu'`/`'mcou'`).
- If code reads `collect(engine='streaming')`, keep streaming-compatible expressions.
- Don't attempt to run integration flows that require `BASE_DATA` unless the file is present; instead, stub/mocks or add an option to point at a local test fixture.

8) Useful files to open next
- `app_beta.py` — marimo cells and UI wiring
- `scratch.py` — data loading, filters, expressions
- `figures.py` — chart rendering (Plotly)
- `config.py` — where BASE_DATA path is configured

If any section is unclear or you want more detail (examples of adding a metric, a test fixture, or a small mock dataset for CI), tell me which part and I'll iterate.
