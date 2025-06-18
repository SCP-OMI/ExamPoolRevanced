#!/usr/bin/env python

import os
import sys
from termcolor import colored

BASEDIR = os.path.join(sys.path[0], "..")
CORRECTIONSDIR = os.path.join(BASEDIR, "corrections")

for item in os.listdir(CORRECTIONSDIR):
    path = os.path.join(CORRECTIONSDIR, item)
    if not os.path.isdir(path):
        continue
    gen = os.path.isfile(os.path.join(path, 'generator.py'))
    print colored(item, "green" if gen else "red")
