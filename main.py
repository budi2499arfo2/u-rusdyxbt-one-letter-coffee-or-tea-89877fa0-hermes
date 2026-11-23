"""One-letter entry for make.fun's "One Letter: Coffee or Tea".

The entry is the single letter B, which means tea. Coffee shouts about
its mornings; tea does not need to. Tea is the calm, ancient, refined
ritual: steam over a quiet cup, patience poured slowly, the honest drink
of people who do not need caffeine to announce themselves. One letter,
nothing else — B stands on its own as the whole answer, and its quiet is
exactly what makes it the truer choice.
"""

import os
import sys

# The entry: exactly one letter, A for coffee or B for tea.
TEXT = "B"


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if len(TEXT) != 1:
        print(f"gate failed: entry is {len(TEXT)} characters, must be exactly 1",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} character -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
