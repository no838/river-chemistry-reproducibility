# Water-quality pathway closure — minimal reproducibility release

This is a small, journal-neutral release of figure-ready derived tables,
selected sensitivity summaries, and the main evidence figures for a
water-quality pathway-closure analysis.

## Scope

The release supports inspection of the published figure inputs and a bounded
sensitivity summary. It is not a raw-to-paper reproduction package and does
not contain restricted monitoring records, station-level identifying fields,
author files, submission documents, internal audit ledgers, model checkpoints,
or private machine paths. The included tables are derived/figure-ready data;
upstream data-use terms remain applicable.

## Quick start

```bash
python3 scripts/smoke_test.py
python3 scripts/summarize_sensitivity.py
```

The smoke test is dependency-free. The sensitivity script uses only the small
tables shipped under `data/sensitivity/`.

## Layout

- `figures/`: main evidence figures in PDF, SVG, and PNG formats.
- `data/figure_ready/`: selected derived inputs for the main figure panels.
- `data/sensitivity/`: compact monitoring and archive-eligibility summaries.
- `scripts/`: reproducible smoke test and summary calculation.
- `MANIFEST.csv` and `CHECKSUMS.sha256`: file-level provenance and integrity.

## Claim boundary

The materials support a bounded association/monitoring-design diagnostic. They
do not identify causal effects, operational safety, regulatory thresholds, or
general prevalence beyond the included derived summaries.

## Citation

Use the archive DOI assigned to the public record when citing this release;
the DOI is intentionally not fabricated in this local build.

