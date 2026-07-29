# River chemistry reproducibility materials

This is a minimal public release of analysis code and figure-ready derived
tables for the study *River water quality separates persistent local states
from collective storm responses*.

It is intentionally not a full raw-data release. The controlled Chinese
four-hour concentration records, station names, exact station coordinates,
internal manuscript files, reviewer materials, package QA records and private
execution traces are excluded.

## Contents

- `code/analysis_reproducibility/`: selected analysis scripts, configuration and
  environment information.
- `data/figure_ready/`: aggregate or pseudonymised figure-ready tables for the
  main evidence panels.
- `data/robustness/`: selected aggregate robustness tables.
- `docs/`: public data-scope and reproduction-boundary notes.
- `scripts/smoke_test.py`: dependency-light package integrity test.
- `SHA256SUMS.txt`: checksums for the release files.

## Reproduction boundary

The package supports inspection of the distributed figure-ready tables and
code provenance. It does not claim unrestricted raw-to-paper reproduction.
Full re-estimation of the Chinese concentration panel requires access to
controlled source records and is outside this release.

The included external-series code may require fresh access to the relevant
public data service. It does not bundle a complete external raw cache.

## Quick check

From the repository root:

```bash
python scripts/smoke_test.py --root .
```

The test writes `QA/smoke_test.json` and checks that the expected code,
configuration and aggregate-data files exist and contain readable tabular
headers.

## Environment

The reference environment is recorded in
`code/analysis_reproducibility/environment.yml` and
`code/analysis_reproducibility/software_environment.json`.

## Data and code availability boundary

This release provides selected code and derived, figure-ready data. It does
not provide the restricted raw Chinese monitoring panel or promise access to
records that are governed by a separate data-custodian review route.

## License and citation

The code is released under the MIT License. The selected derived figure-ready
tables are released under CC BY 4.0; upstream-data conditions and the excluded
controlled raw records are not changed by this release. See `LICENSE`,
`LICENSE-DATA.md` and `CITATION.cff`.
