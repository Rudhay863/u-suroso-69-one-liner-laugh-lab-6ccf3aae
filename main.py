#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the robot vacuum's excuse after eating a sock."""

import os

LINE = "The sock was on the floor, so under house rules it was legally floor food — and I don't make the rules, I just vacuum them."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
