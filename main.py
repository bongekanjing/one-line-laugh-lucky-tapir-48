"""Emit the one-line joke for the laugh bounty into entry.txt.

One sentence lives here as a constant. The rest of the file only decides where
to put it and refuses to write anything the gate would reject. No network, no
clock, so the output is stable across runs.
"""

import os

JOKE = (
    "I named my houseplant after my ex so I could finally keep something "
    "alive out of spite."
)

MAX_CHARS = 200


def flatten(raw):
    """Strip the source formatting down to a single spaced line."""
    pieces = raw.split()
    return " ".join(pieces)


def guard(text):
    """Reject blank, whitespace-only or over-long text before it reaches disk."""
    if len(text) < 1:
        raise ValueError("the joke is empty")
    if text.strip() == "":
        raise ValueError("the joke is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("the joke runs to %d characters, cap is %d"
                         % (len(text), MAX_CHARS))
    return text


def output_path():
    """Honour the grader's folder when it sets one."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    return os.path.join(folder, "entry.txt")


def main():
    text = guard(flatten(JOKE))
    path = output_path()
    holder = os.path.dirname(path)
    if holder:
        os.makedirs(holder, exist_ok=True)
    handle = open(path, "w", encoding="utf-8", newline="\n")
    try:
        handle.write(text)
        handle.write("\n")
    finally:
        handle.close()
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
