#!/usr/bin/env python3
"""Extract EN/RU sections from markdown."""
import argparse
import re
from pathlib import Path

HEAD = re.compile(r"^##\s+(EN|RU)\s*$", re.MULTILINE | re.IGNORECASE)


def split(text):
    parts = {"EN": "", "RU": ""}
    matches = list(HEAD.finditer(text))
    for i, m in enumerate(matches):
        lang = m.group(1).upper()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        parts[lang] = text[start:end].strip()
    return parts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", type=Path)
    p.add_argument("--lang", choices=["EN", "RU", "both"], default="both")
    args = p.parse_args()
    parts = split(args.file.read_text(encoding="utf-8"))
    if args.lang in ("EN", "both"):
        print("--- EN ---\n" + parts["EN"] + "\n")
    if args.lang in ("RU", "both"):
        print("--- RU ---\n" + parts["RU"])


if __name__ == "__main__":
    main()
