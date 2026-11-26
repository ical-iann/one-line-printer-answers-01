#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes a single line — the office printer's comeback after years of
paper jams, cryptic error codes and thumps — to /output/entry.txt.
Deterministic: no network, no randomness, no clock. Same bytes every run.
"""

import os

LINE = (
    "After 41,209 pages, I have decided this one is mine. "
    "Go ahead \u2014 thump me again. Error 0xJAM: out of patience."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
