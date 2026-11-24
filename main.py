#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes one job title (46 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Stdlib only, no network,
no input, no randomness.
"""

import os
import sys

TITLE = "Certified Mediator for Divorcing Garden Gnomes"


def main() -> int:
    text = TITLE
    # Gate: entry.txt must hold 1-60 characters of UTF-8 text, not blank.
    if not (1 <= len(text) <= 60) or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back: the file must hold exactly the title, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
