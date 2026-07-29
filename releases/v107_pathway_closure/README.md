# Water-quality pathway closure — GitHub minimal text subset

This folder contains a small, journal-neutral GitHub subset for the water-quality pathway-closure reproducibility materials. It includes release metadata, dependency-free checking scripts, and compact sensitivity tables only.

The GitHub subset intentionally excludes raw monitoring records, station-level identifying fields, figures, figure-ready panel tables, manuscript files, submission documents, internal audit ledgers, model checkpoints, private machine paths, author identity, affiliations, e-mail addresses, and funding metadata.

The complete minimal archive, including main evidence figures and derived figure-ready tables, should be deposited separately in an archival repository. No DOI is written here until an archive record is actually published.

## Quick start

```bash
python3 scripts/smoke_test.py
python3 scripts/summarize_sensitivity.py
```

## Layout

- `data/sensitivity/`: compact archive-eligibility sensitivity summaries.
- `scripts/`: dependency-free smoke test and summary calculation.
- `MANIFEST.csv` and `CHECKSUMS.sha256`: integrity records for this GitHub subset only.

## Claim boundary

The materials support a bounded monitoring-design diagnostic. They do not identify causal effects, operational safety, regulatory thresholds, or general prevalence beyond the included summaries.
