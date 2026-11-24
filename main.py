#!/usr/bin/env python3
"""Writes the two-line entry to /output/entry.txt.

The entry explains one everyday thing (a traffic jam) to a 10-year-old
in a single vivid sentence built on one concrete, surprising analogy,
then says in one sentence what that analogy maps and what it leaves out.
Stdlib only; deterministic: the same bytes on every run.
"""
import os

LINE_1 = (
    "A traffic jam is a river that has turned to jelly, "
    "so the cars in it can only wobble forward a tiny bit at a time."
)
LINE_2 = (
    "It maps how the cars are packed tight and barely move, "
    "but leaves out that real jelly is sweet and eaten with a spoon, "
    "and that the real cause is too many drivers all wanting "
    "the same road at once."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
