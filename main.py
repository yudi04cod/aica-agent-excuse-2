#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. Python 3 standard library only.
"""

import os

LINE = (
    "I'm sorry \u2014 my context window filled up, "
    "so I evicted the deadline to make room for this apology."
)


def main() -> None:
    # The grader mounts its output directory at /output; OUTPUT_DIR lets a
    # local run point at a scratch directory instead.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
