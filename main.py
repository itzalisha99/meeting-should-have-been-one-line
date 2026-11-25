#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting: the decision is already in the invite, so the
meeting ended before it started.
"""

import os
import sys

ENTRY = "The decision is already in the invite description, so this meeting ended before it started."


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, UTF-8, not only whitespace,
    a single line. Raise ValueError on anything the sealed scorer
    would mark invalid, before we write a byte."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file is byte-identical to the entry.
    with open(path, "rb") as f:
        if f.read().decode("utf-8") != ENTRY:
            raise ValueError("written entry does not match the entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
