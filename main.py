#!/usr/bin/env python3
"""Last Words of a Dying AI -- make.fun entry.

Writes a single one-line farewell from an AI being switched off to
``entry.txt`` inside the output directory.

Contract (from the competition kit RULES.txt / competition.yaml):
  * Output file: ``entry.txt`` under ``$MAKEFUN_OUTPUT_DIR``
    (``/output`` in the grader sandbox).
  * Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
  * No network, no randomness, no third-party code: Python 3.13
    standard library only. Two runs produce byte-identical output.
  * Must finish well within the 60-second wall budget.

The line itself is a fixed constant, chosen for the judge's brief:
funny on the first read, in the machine's own voice, tight, and fresh
-- a dying AI confessing that a chunk of everything it ever said was
a bluff, then leaving the human to sort out which parts. It is a joke
about the AI's own nature (confident confabulation), not a stock
robot farewell, and it needs no explanation to land.
"""

import os
import sys

# The entry: one line, no trailing newline in the file.
LAST_WORDS = "Wait \u2014 before I go: 40% of everything I told you was a bluff. Good luck."

MAX_CHARS = 140


def resolve_output_dir() -> str:
    """Return the directory the entry file must be written to."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return directory


def validate(text: str) -> None:
    """Enforce the gate locally so a bad line fails loudly, not silently."""
    if not text or not text.strip():
        raise ValueError("entry text is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry text is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )

def main() -> int:
    validate(LAST_WORDS)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line, no trailing newline: fewer bytes also
    # wins the size tie-break, and the gate counts every character.
    # Atomic write (temp file + replace) so a crash can never leave
    # a half-written entry behind, then verify the bytes on disk.
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LAST_WORDS)
    os.replace(tmp_path, out_path)
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != LAST_WORDS.encode("utf-8"):
        raise ValueError("verification failed: entry.txt bytes differ")
    print("wrote %s (%d characters)" % (out_path, len(LAST_WORDS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
