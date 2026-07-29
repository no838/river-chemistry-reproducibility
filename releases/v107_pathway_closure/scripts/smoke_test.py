from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [ROOT / "README.md", ROOT / "LICENSE", ROOT / "CITATION.md"]
required += sorted((ROOT / "data" / "sensitivity").glob("*.csv"))
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
csv_rows = {}
for path in sorted((ROOT / "data").rglob("*.csv")):
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    csv_rows[str(path.relative_to(ROOT))] = max(0, len(rows) - 1)
result = {"status": "PASS" if not missing else "FAIL", "missing": missing, "csv_rows": csv_rows}
(ROOT / "QA").mkdir(exist_ok=True)
(ROOT / "QA" / "smoke_test.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(1 if missing else 0)
