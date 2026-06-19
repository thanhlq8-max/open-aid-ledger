#!/usr/bin/env python3
"""Generate a simple Markdown transparency report.

This script is intentionally read-only:
- no wallet signing
- no transfers
- no private keys
- no exchange APIs
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing CSV file: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _amount(row: dict[str, str]) -> Decimal:
    raw = (row.get("amount") or "").strip()
    if not raw:
        return Decimal("0")
    try:
        return Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid amount {raw!r} in row: {row}") from exc


def _sum_by_asset(rows: Iterable[dict[str, str]]) -> dict[tuple[str, str, str], Decimal]:
    totals: dict[tuple[str, str, str], Decimal] = defaultdict(Decimal)
    for row in rows:
        key = (
            (row.get("chain") or "UNKNOWN").strip(),
            (row.get("asset") or "UNKNOWN").strip(),
            (row.get("network") or "UNKNOWN").strip(),
        )
        totals[key] += _amount(row)
    return dict(totals)


def _format_totals(title: str, totals: dict[tuple[str, str, str], Decimal]) -> list[str]:
    lines = [f"## {title}", ""]
    if not totals:
        lines.append("No records.")
        lines.append("")
        return lines

    lines.extend(["| Chain | Asset | Network | Amount |", "|---|---|---|---:|"])
    for (chain, asset, network), amount in sorted(totals.items()):
        lines.append(f"| {chain} | {asset} | {network} | {amount.normalize()} |")
    lines.append("")
    return lines


def generate_report(donations_path: Path, disbursements_path: Path) -> str:
    donations = _read_csv(donations_path)
    disbursements = _read_csv(disbursements_path)

    donation_totals = _sum_by_asset(donations)
    disbursement_totals = _sum_by_asset(disbursements)

    lines: list[str] = [
        "# Open Aid Ledger Transparency Report",
        "",
        "This report is generated from public CSV records.",
        "",
        "## Scope",
        "",
        "- Read-only report.",
        "- No trading.",
        "- No investment.",
        "- No custody automation.",
        "- No private beneficiary data.",
        "",
        "## Record counts",
        "",
        f"- Donation records: {len(donations)}",
        f"- Disbursement records: {len(disbursements)}",
        "",
    ]

    lines.extend(_format_totals("Incoming donations by asset", donation_totals))
    lines.extend(_format_totals("Outgoing support by asset", disbursement_totals))

    lines.extend([
        "## Privacy note",
        "",
        "Beneficiaries should be identified by codes, not raw personal information.",
        "",
        "## Legal note",
        "",
        "This report is not legal, tax, accounting, financial, or investment advice.",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Open Aid Ledger Markdown report.")
    parser.add_argument("--donations", required=True, type=Path)
    parser.add_argument("--disbursements", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    report = generate_report(args.donations, args.disbursements)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report, encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
