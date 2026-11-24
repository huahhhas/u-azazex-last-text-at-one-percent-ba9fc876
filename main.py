#!/usr/bin/env python3
"""Last text at one percent for make.fun's Last Text at One Percent.

Writes the dying phone's final text message (one line, under
200 characters) to /output/entry.txt.
"""

import os

LINE = "1%. This is my last text. Charger, I never loved you back. Group chat, I died doing what I loved: ignoring you."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
