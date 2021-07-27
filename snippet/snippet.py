#!/usr/bin/env python

from pathlib import Path
from sys import argv
import re


def main():
    scriptdir = Path(__file__).resolve().parent

    with open(scriptdir.joinpath("data.py")) as f:
        headptn = re.compile(r"# \w+ :: .*")
        snippet_dict = {}
        key = None
        comment = None
        codes = []
        for line in f:
            if headptn.match(line):
                if key:
                    snippet_dict[key] = (comment, codes)
                key, comment = line.split("::")[0:2]
                key = key.rstrip()[2:]
                comment = comment.strip()
                codes = []
            else:
                codes.append(line.rstrip())
        if (len(argv) <= 1) or not (argv[1] in snippet_dict):
            for key, value in sorted(snippet_dict.items()):
                print(f"{key}    {value[0]}")
        else:
            print("\n".join(snippet_dict[argv[1]][1]))


if __name__ == "__main__":
    main()
