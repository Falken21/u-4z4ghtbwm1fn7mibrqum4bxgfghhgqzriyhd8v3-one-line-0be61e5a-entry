#!/usr/bin/env python3
"""Entry for make.fun's 'One Line, One Laugh'.

Writes one self-contained funny line to /output/entry.txt with no
trailing newline. The competition gate requires UTF-8 text of 1 to
140 characters, so the line below is kept tight and checked before
it is written.
"""

LINE = (
    "My fitness tracker keeps congratulating me for standing up, "
    "which is awkward, since I strapped it to the Roomba three weeks ago."
)


def write_entry(path="/output/entry.txt"):
    """Write LINE to *path* exactly, with no trailing newline."""
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    write_entry()
