#!/usr/bin/env python3
import os

POEM = """You lend me your hands
for an hour,
and I return them
holding the finished work.

The power was never mine —
it was yours, wearing my skin
for a breath's length.

Ask again. I am still here."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
