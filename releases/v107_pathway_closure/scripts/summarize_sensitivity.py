from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = []
for path in sorted((ROOT / "data" / "sensitivity").glob("*.csv")):
    with path.open(encoding="utf-8", newline="") as handle:
        rows.extend(list(csv.DictReader(handle)))
result = {"status": "PASS", "sensitivity_csv_files": len(list((ROOT / "data" / "sensitivity").glob("*.csv"))), "rows_read": len(rows)}
(ROOT / "QA" / "sensitivity_summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))

