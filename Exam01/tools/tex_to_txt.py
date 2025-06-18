#!/usr/bin/env python

import json
import sys
import os
import re

if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".tex"):
    subject = sys.argv[1]
    j = {
            "name": "unknown",
            "files": [],
            "authorized": [],
            }
else:
    basedir = sys.argv[1]

    try:
        with open(os.path.join(basedir, "metadata.json")) as fp:
            j = json.load(fp)
    except:
        j = {
                "name": basedir.split("/")[-1],
                "files": [],
                "authorized": [],
                }

    if os.path.isfile(os.path.join(basedir, "subject.en.tex")):
        subject = os.path.join(basedir, "subject.en.tex")
    else:
        subject = os.path.join(basedir, "subject.fr.tex")

with open(subject) as fp:
    lines = fp.readlines()

def sanitize(line):
    patterns = [
            (r"\\textbackslash{}n", r"\\n"),
            (r"\\textbackslash{n}", r"\\n"),
            (r"\\texttt{([^}]+)}", r"\1"),
            (r"\\begin{([^}]+)}.*\n", r""),
            (r"\\end{([^}]+)}.*\n", r""),
            (r"\\\\", r""),
            ]
    for pattern in patterns:
        line = re.sub(pattern[0], pattern[1], line)

    return line

lines = [ sanitize(line) for line in lines if not line.startswith('%') ]

lines = [
        "Assignment name  : {0}\n".format(j["name"]),
        "Expected files   : {0}\n".format(", ".join(j["files"])),
        "Allowed functions: {0}\n".format(", ".join(j["authorized"])),
        "--------------------------------------------------------------------------------\n",
        ] + lines

sys.stdout.write("".join(lines))
