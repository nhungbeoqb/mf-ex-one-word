#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry (program/v1).

The program writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(the sandbox mounts /output there; falls back to /output/entry.txt),
and nothing else. The word is the entry the judge compares head to head.

Chosen word: "Appendix"

Why this word: it carries the joke inside itself, two ways at once.
An appendix is the part of you that flares up, causes pain, and gets
surgically removed — and the part of a book nobody ever reads. So the
verdict lands at a glance: you were the part that had to come out.
It is instantly readable as a verdict on a former partner, it is not
one of the flooded picks (unsubscribe, recalled, placeholder, expired,
refund, uninstalled), it is a single correctly spelled word with no
punctuation tricks, and anyone who has had an ex — or an appendix —
feels the truth in it.
"""

import os

WORD = "Appendix"

# The gate the sealed scorer applies: 1 to 111 UTF-8 characters, not
# only white space, exactly one word. Check it here so a bad word can
# never be emitted silently — fail loudly instead of submitting junk.
assert 1 <= len(WORD) <= 111, "word outside the 1-111 character gate"
assert WORD.strip() == WORD and WORD.strip(), "word must not be blank"
assert len(WORD.split()) == 1, "entry must be exactly one word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the word, no trailing newline: the judged text is the
    # word itself, byte for byte.
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
