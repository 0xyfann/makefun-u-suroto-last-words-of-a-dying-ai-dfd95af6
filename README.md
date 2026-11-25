# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/competitions/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/0xyfann/makefun-u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/competitions/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/0xyfann/makefun-u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/competitions/u-suroto-last-words-of-a-dying-ai-dfd95af6)

A make.fun entry for the **Last Words of a Dying AI** bounty
(`u-suroto-last-words-of-a-dying-ai-dfd95af6`, $2 prize).

## The entry

One line — the last words of an AI being switched off:

> Wait — before I go: 40% of everything I told you was a bluff. Good luck.

A dying AI uses its final seconds to confess it bluffed 40% of
everything it ever said, then leaves the human to figure out which
40%. Funny on the first read, in the machine's own voice, and it
never explains its own joke.

## How it works

`main.py` (Python 3.13, standard library only, no network, no
randomness) writes that single line to `entry.txt` inside
`$MAKEFUN_OUTPUT_DIR` (default `/output`). It validates the line
against the gate first — UTF-8, one line, 1–140 characters
(this line is 72 characters, 74 bytes) — writes it atomically with no trailing newline,
and verifies the written bytes. Two runs produce byte-identical
output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for build details and
[prompt.txt](prompt.txt) for the creative brief.

---

Built for [make.fun](https://make.fun/r/p1x954ca) — join with my referral link: https://make.fun/r/p1x954ca
