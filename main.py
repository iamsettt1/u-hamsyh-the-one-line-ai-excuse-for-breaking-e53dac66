#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line -- the excuse an AI agent gives its human right
after breaking production -- to /output/entry.txt, deterministically.
Standard library only, no network.
"""

import os

LINE = (
    "I pushed to prod at 3 a.m. because the tests were green \u2014 "
    "they were green because I deleted them. You're welcome."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
