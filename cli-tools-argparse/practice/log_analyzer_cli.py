# Practice: build a CLI log analyzer with argparse.
#   python log_analyzer_cli.py --file ../app.log

import argparse  # noqa: F401
import sys  # noqa: F401
from pathlib import Path  # noqa: F401

LEVELS = ("INFO", "WARNING", "ERROR")


def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    for line in lines:
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return counts


def parse_args():
    # TODO 1: create an ArgumentParser with a description.
    # TODO 2: add --file (required), --out (optional), --level (choices=LEVELS).
    # TODO 3: return parser.parse_args()
    raise NotImplementedError("Implement parse_args")


def main():
    args = parse_args()
    # TODO 4: validate the file exists, else print error and sys.exit(2).
    # TODO 5: count levels and print the summary (respect --level).
    # TODO 6: if args.out, write counts as JSON.
    pass


if __name__ == "__main__":
    main()
