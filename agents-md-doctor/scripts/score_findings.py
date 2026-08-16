#!/usr/bin/env python3
"""Calculate deterministic AGENTS.md audit scores from finding JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MAXIMUMS = {
    "consistency": 25,
    "clarity": 20,
    "conciseness": 15,
    "actionability": 15,
    "scope": 15,
    "safety": 10,
}
DEDUCTIONS = {"critical": 10, "high": 6, "medium": 3, "low": 1}


def load_payload(path: str | None) -> object:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return json.load(sys.stdin)


def calculate(payload: object) -> dict[str, object]:
    if isinstance(payload, dict):
        findings = payload.get("findings")
    else:
        findings = payload
    if not isinstance(findings, list):
        raise ValueError("input must be a list or an object with a findings list")

    scores = dict(MAXIMUMS)
    seen_ids: set[str] = set()
    seen_fingerprints: set[str] = set()
    applied: list[dict[str, object]] = []

    for index, finding in enumerate(findings, start=1):
        if not isinstance(finding, dict):
            raise ValueError(f"finding {index} must be an object")
        finding_id = finding.get("id")
        fingerprint = finding.get("fingerprint")
        dimension = finding.get("dimension")
        severity = finding.get("severity")
        if not isinstance(finding_id, str) or not finding_id:
            raise ValueError(f"finding {index} has no non-empty id")
        if finding_id in seen_ids:
            raise ValueError(f"duplicate finding id: {finding_id}")
        seen_ids.add(finding_id)
        if not isinstance(fingerprint, str) or not fingerprint:
            raise ValueError(f"finding {finding_id} has no non-empty fingerprint")
        if fingerprint in seen_fingerprints:
            continue
        seen_fingerprints.add(fingerprint)
        if dimension not in MAXIMUMS:
            raise ValueError(f"finding {finding_id} has invalid dimension: {dimension}")
        if severity not in DEDUCTIONS:
            raise ValueError(f"finding {finding_id} has invalid severity: {severity}")
        deduction = DEDUCTIONS[severity]
        scores[dimension] = max(0, scores[dimension] - deduction)
        applied.append(
            {
                "id": finding_id,
                "fingerprint": fingerprint,
                "dimension": dimension,
                "severity": severity,
                "deduction": deduction,
            }
        )

    total = sum(scores.values())
    grade = "A" if total >= 90 else "B" if total >= 80 else "C" if total >= 70 else "D" if total >= 60 else "F"
    return {"total": total, "grade": grade, "scores": scores, "applied_findings": applied}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="JSON file; omit to read stdin")
    args = parser.parse_args()
    try:
        result = calculate(load_payload(args.path))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
