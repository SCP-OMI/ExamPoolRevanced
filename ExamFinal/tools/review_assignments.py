#!/usr/bin/env python

import sys
import os
import yaml

BASEDIR = os.path.join(sys.path[0], "..")
CORRECTIONSDIR = os.path.join(BASEDIR, "corrections")
SUBJECTSDIR = os.path.join(BASEDIR, "subjects")
POOLSDIR = os.path.join(BASEDIR, "pools")
DOCSDIR = os.path.join(BASEDIR, "docs")

with open(sys.argv[1]) as fp:
    data = yaml.load(fp)

for level in data["levels"]:
    for ass in level["assignments"]:
        with open(os.path.join(SUBJECTSDIR, ass, "subject.en.txt")) as fp:
            print fp.read()
        print
        print
        raw_input("Press Enter to continue ...")


