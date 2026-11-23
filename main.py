"""The One-Line Laugh entry.

Writes one funny line, a single sentence, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is held here as a constant so the program is
self-contained: no network, no files read, standard library only.
"""

import os

LINE = "My smartwatch congratulated me for standing up, which is the only applause I have received all year."

OUTPUT_NAME = "entry.txt"


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would reject:
    # the line must be one sentence of 1-200 characters, not only whitespace.
    text = LINE.strip()
    if not 1 <= len(text) <= 200 or not text or text != LINE:
        raise SystemExit("entry line fails the 1-200 character gate")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise SystemExit("entry line must be a single sentence")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
