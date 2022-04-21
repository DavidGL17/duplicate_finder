#!/usr/bin/env python
""" Converts all webp image files into png (stores webp in separate folder for easy removal)
"""
from argparse import ArgumentParser
from PIL import Image
from pathlib import Path


def processPath(path):
    for file in sorted(Path(path).glob("**.webp")):
        print(file)


parser = ArgumentParser()
parser.add_argument("paths", type=str, nargs="*", help="the paths to analyse")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    for path in args.paths:
        processPath(path)
