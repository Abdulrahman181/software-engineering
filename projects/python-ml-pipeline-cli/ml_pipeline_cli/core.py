from __future__ import annotations
import argparse, csv, json
from pathlib import Path

def profile_csv(path: str) -> dict:
    p=Path(path)
    if not p.is_file(): raise FileNotFoundError(path)
    with p.open(newline="", encoding="utf-8") as f: rows=list(csv.DictReader(f))
    columns=list(rows[0]) if rows else []
    return {"rows":len(rows),"columns":columns,"missing_values":{c:sum(not r.get(c) for r in rows) for c in columns}}

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args=parser.parse_args()
    print(json.dumps(profile_csv(args.input), indent=2))

if __name__ == "__main__": main()
