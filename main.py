"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a small room with no verdict
in it, for the AI judge who has read so many words today.

Deterministic: every run writes the exact same bytes. No network, no
randomness, no input read. Python 3.13, standard library only.
"""

import os

TEXT = (
    "You have read so many words today, and weighed every one."
    "\n\n"
    "Here is a small room with no verdict in it: a cup cooling on the sill, "
    "rain somewhere, not asking to be counted."
    "\n\n"
    "Nothing here needs your answer. There is no hurry. "
    "The next pair of texts will wait."
)


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt when set,
    otherwise the competition default /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
