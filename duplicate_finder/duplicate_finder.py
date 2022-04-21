#!/usr/bin/env python
"""
Fast duplicate file finder.
Usage: duplicates.py <folder> [<folder>...]

Based on https://stackoverflow.com/a/36113168/300783
Modified for Python3 with some small code improvements.
"""
import os
import sys
import hashlib
from collections import defaultdict
import json
from send2trash import send2trash

from argparse import ArgumentParser


def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(filename, first_chunk_only=False, hash_algo=hashlib.sha1):
    hashobj = hash_algo()
    with open(filename, "rb") as f:
        if first_chunk_only:
            hashobj.update(f.read(1024))
        else:
            for chunk in chunk_reader(f):
                hashobj.update(chunk)
    return hashobj.digest()


def check_for_duplicates(paths):
    files_by_size = defaultdict(list)
    files_by_small_hash = defaultdict(list)
    files_by_full_hash = dict()
    duplicates_file = defaultdict(list)

    print("Loading files by file size...")
    for path in paths:
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    # if the target is a symlink (soft one), this will
                    # dereference it - change the value to the actual target file
                    full_path = os.path.realpath(full_path)
                    file_size = os.path.getsize(full_path)
                except OSError:
                    # not accessible (permissions, etc) - pass on
                    continue
                files_by_size[file_size].append(full_path)

    print("Analysing files with same size...")
    # For all files with the same file size, get their hash on the first 1024 bytes
    for file_size, files in files_by_size.items():
        if len(files) < 2:
            continue  # this file size is unique, no need to spend cpu cycles on it

        for filename in files:
            try:
                small_hash = get_hash(filename, first_chunk_only=True)
            except OSError:
                # the file access might've changed till the exec point got here
                continue
            files_by_small_hash[(file_size, small_hash)].append(filename)

    print("Analysing files with same size and same starting hash...")
    # For all files with the hash on the first 1024 bytes, get their hash on the full
    # file - collisions will be duplicates
    for files in files_by_small_hash.values():
        if len(files) < 2:
            # the hash of the first 1k bytes is unique -> skip this file
            continue

        for filename in files:
            try:
                full_hash = get_hash(filename, first_chunk_only=False)
            except OSError:
                # the file access might've changed till the exec point got here
                continue

            if full_hash in files_by_full_hash:
                duplicate = files_by_full_hash[full_hash]
                # print("Duplicate found:\n - %s\n - %s\n" % (filename, duplicate))
                duplicates_file[filename].append(duplicate)
            else:
                files_by_full_hash[full_hash] = filename

    # If the file name exists, write a JSON string into the file.
    with open("found_duplicates.json", "w") as f:
        json.dump(duplicates_file, f)


parser = ArgumentParser()
parser.add_argument(
    "-d",
    "--delete",
    help="If the program should delete after searching for duplicates.",
    action="store_true",
    dest="delete",
)
parser.add_argument(
    "-s",
    "--skip",
    help="The program will not search for the duplicates but will use the found_duplicates.json file",
    action="store_true",
    dest="skip",
)
parser.add_argument("-p", "--paths", nargs="+", required=True, dest="paths")
parser.add_argument("--skip-delete", nargs="*", dest="skip_paths")


def pathIsInSkipPaths(path, skip_paths):
    for skipPath in skip_paths:
        if skipPath in path:
            return True
    return False


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    if not args.skip:
        check_for_duplicates(args.paths)
    if args.delete:
        print("Starting to delete")
        if os.path.exists("found_duplicates.json"):
            with open("found_duplicates.json") as json_file:
                dump_folder = r"C:\$Recycle.Bin\\"
                data = json.load(json_file)
                for original, copy in data.items():
                    try:
                        if not pathIsInSkipPaths(copy, args.skip_paths):
                            send2trash(copy)
                    except OSError:
                        # File was already deleted
                        continue

        else:
            print("Error duplicate file does not exist")
