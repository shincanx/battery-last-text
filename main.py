#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — one-line last text message.

Writes the battery's last text as a single line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it.
Fully deterministic: a fixed string, no clock, no randomness, no network.
"""

import os

LINE = "I held 3% all day while you scrolled, and now you want a goodbye speech? Plug me in, coward \u2014 I have 40 seconds of dignity left."


def main() -> None:
    line = LINE
    assert "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line.strip() == line and line, "line must not be blank or padded"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
