#!/usr/bin/env python

import sys
import os
import yaml

from termcolor import colored

BASEDIR = os.path.join(sys.path[0], "..")
CORRECTIONSDIR = os.path.join(BASEDIR, "corrections")
SUBJECTSDIR = os.path.join(BASEDIR, "subjects")
POOLSDIR = os.path.join(BASEDIR, "pools")
DOCSDIR = os.path.join(BASEDIR, "docs")

def check_pool(pool):
    with open(pool) as fp:
        data = yaml.load(fp)

    seen = []
    errors = []
    ok = True
    if "docs" not in data:
        ok = False
        errors.append("Pool has no docs field")
    elif not os.path.isdir(os.path.join(DOCSDIR, data["docs"])):
        ok = False
        errors.append("Docs {0} dir does not exist".format(data["docs"]))
    for level in data["levels"]:
        for ass in level["assignments"]:
            cd = os.path.join(CORRECTIONSDIR, ass)
            sd = os.path.join(SUBJECTSDIR, ass)
            if not os.path.isdir(sd):
                ok = False
                errors.append("{0} has no subject (Should be in {1})".format(ass, sd))
            if not os.path.isdir(cd):
                ok = False
                errors.append("{0} has no correction (Should be in {1})".format(ass, cd))
            elif not os.path.isfile(os.path.join(cd, "profile.yml")):
                ok = False
                errors.append("{0} has no profile.yml file (Should be in {1})".format(ass, cd))
            if ass in seen:
                ok = False
                errors.append("{0} appears more than once in the pool".format(ass))
            seen.append(ass)

    return (ok, errors)

allok = True
for item in os.listdir(POOLSDIR):
    if not item.endswith(".yml"):
        continue
    (ok, errors) = check_pool(os.path.join(POOLSDIR, item))
    print "Pool '{0}': {1}".format(
        (item.split(".")[0]),
        colored("ok", "green") if ok else colored("KO", "red")
    )
    if not ok:
        allok = False
        for error in errors:
            print "  - {0}".format(error)

sys.exit(1 if not allok else 0)
