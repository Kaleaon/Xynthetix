"""CLI: python -m braid <file.braid.json> [more files...]

Prints the simulator summary for each spec. Exit code 1 if any file fails.
"""

from __future__ import annotations

import sys

from .geometry import simulate
from .spec import SpecError, load_spec


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    status = 0
    for arg in argv:
        try:
            result = simulate(load_spec(arg))
        except SpecError as exc:
            print(f"{arg}: {exc}", file=sys.stderr)
            status = 1
            continue
        print(result.summary())
        print()
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
