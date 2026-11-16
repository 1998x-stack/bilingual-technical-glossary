"""Check that all fields in the canonical glossary JSON survive CSV export.

The check is intentionally independent of the repository's real data so that
regression tests can exercise malformed inputs without editing publications.
"""
from collections.abc import Mapping, Sequence


def csv_differences(terms: Sequence[Mapping], fieldnames, rows, limit=25):
    """Return a bounded list of missing columns, count or cell mismatches."""
    errors = []
    columns = list(fieldnames or ())
    expected = set().union(*(set(row) for row in terms)) if terms else set()

    if not columns or len(columns) != len(set(columns)):
        errors.append("CSV has missing or duplicated header fields")
    missing = sorted(expected - set(columns))
    unexpected = sorted(set(columns) - expected)
    if missing:
        errors.append("CSV missing JSON fields: " + ", ".join(missing))
    if unexpected:
        errors.append("CSV has unknown fields: " + ", ".join(unexpected))
    if len(rows) != len(terms):
        errors.append(f"CSV row count {len(rows)} differs from JSON {len(terms)}")

    for index, (term, csv_row) in enumerate(zip(terms, rows), 1):
        if None in csv_row:
            errors.append(f"CSV row {index} has extra unmapped columns")
        for field in columns:
            raw = term.get(field, "")
            expected_value = "" if raw is None else str(raw)
            if csv_row.get(field) != expected_value:
                errors.append(
                    f"CSV row {index} field {field!r} does not match canonical JSON"
                )
                if len(errors) >= limit:
                    return errors
        if len(errors) >= limit:
            return errors
    return errors[:limit]
