#!/usr/bin/env python
""" Converts all webp image files into png (stores webp in separate folder for easy removal)
"""
from argparse import ArgumentParser
from PIL import Image
from pathlib import Path
import os

copy_dir = "./copy_dir/"


def processPath(path):
    for file in sorted(Path(path).glob("*.webp")):
        img = Image.open(file)
        img.save(copy_dir + os.path.basename(file))
        newPath = Path(file)
        newPath.rename(newPath.with_suffix(".png"))


parser = ArgumentParser()
parser.add_argument("paths", type=str, nargs="*", help="the paths to analyse")

if __name__ == "__main__":
    # Create copy_dir
    if not os.path.exists(copy_dir):
        os.mkdir(copy_dir)
    args = parser.parse_args()
    if len(args.paths) == 0:
        print("Please provide at least one path")
        exit(0)
    for path in args.paths:
        processPath(path)
