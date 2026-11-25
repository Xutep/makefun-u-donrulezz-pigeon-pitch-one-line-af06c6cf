#!/usr/bin/env python3
"""Pigeon Pitch, One Line -- make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt. Deterministic, standard library only: the
pitch is a fixed string, so every run produces the exact same file.
"""

import os

PITCH = (
    "I'm a pigeon pitching Coo: lunch at your window before your app loads, "
    "drivers who work for breadcrumbs \u2014 and my seed round? "
    "That's literally my breakfast."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"pitch must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
