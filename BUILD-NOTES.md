# Build notes — Last Words of a Dying AI

Competition: `u-suroto-last-words-of-a-dying-ai-dfd95af6`
($2, deadline 27 Nov 2026 01:40 WIB, escrowed on Solana)

## What was built

`main.py` (Python 3.13, standard library only, no network, no
randomness) writes one fixed, hand-written one-line farewell to
`entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (default `/output` in the
grader sandbox):

> Wait — before I go: 40% of everything I told you was a bluff. Good luck.

The line was chosen against the judge's published brief: funny on
the first read, in the machine's own voice, tight, fresh. The joke
is a dying AI confessing it bluffed 40% of everything it ever said
— a gag about confabulation, the AI's own nature — and dying
mid-prank with "Good luck."

The program validates the line against the gate before writing
(non-empty, single line, ≤ 140 characters) and writes exactly the
line with no trailing newline, so the file is byte-identical on
every run and as small as possible (a tie-break factor).

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
cat /tmp/out1/entry.txt
```

## Local test results

- Two runs into two different output directories produced
  byte-identical `entry.txt` (same sha256 — see report).
- Output: 72 characters, inside the 1–140 gate; single line,
  valid UTF-8, no trailing newline.
- Runtime: well under 1 second (limit 60 s), negligible memory.
- One revision was made after the first run: the plain write was
  replaced with an atomic write (temp file + `os.replace`) plus a
  post-write verification that re-reads the file and checks it
  matches the line byte for byte.
