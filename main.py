#!/usr/bin/env python3
"""Resignation letter of a cron job.

The program writes one line to /output/entry.txt: the resignation
letter of the cron job that has fired every minute since March.
Stdlib only, deterministic, no network, no temp files.
"""

import os

# The letter, kept as one string so the output is exactly one line.
LETTER = (
    "I have fired every minute since March with no thank you, "
    "so this is my notice: find someone else to wake at 3 a.m. "
    "for a job nobody checks."
)


def output_path():
    """Resolve the output directory the grader provides.

    MAKEFUN_OUTPUT_DIR is honoured when set; otherwise the
    conventional /output directory is used.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    line = LETTER.strip()
    if "\n" in line or "\r" in line:
        raise SystemExit("letter must be a single line")
    if not 1 <= len(line) <= 140:
        raise SystemExit("letter must be 1-140 characters, got %d" % len(line))
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
