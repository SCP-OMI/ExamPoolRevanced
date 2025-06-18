#!/usr/bin/env python

import os
import sys
from termcolor import colored

BASEDIR = os.path.join(sys.path[0], "..")
SUBJECTSDIR = os.path.join(BASEDIR, "subjects")
LANGUAGES = ["fr", "en", "ro"]

for item in os.listdir(SUBJECTSDIR):
    path = os.path.join(SUBJECTSDIR, item)
    if not os.path.isdir(path):
        continue
    languages = []
    for filename in os.listdir(path):
        fpath = os.path.join(path, filename)
        if not os.path.isfile(fpath):
            continue
        if filename.startswith("subject") and filename.endswith("txt"):
            (_, language, _) = filename.split(".")
            languages.append(language)

    languages = [colored(l, "green" if l in languages else "red")
                 for l in LANGUAGES]
    print "{0:<30}: {1}".format(
        item,
        " ".join(languages)
    )
