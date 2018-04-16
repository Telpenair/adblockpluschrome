#!/usr/bin/env python
# coding: utf-8

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPENDENCY_SCRIPT = os.path.join(BASE_DIR, "ensure_dependencies.py")

try:
    subprocess.check_call([sys.executable, DEPENDENCY_SCRIPT, BASE_DIR])
except subprocess.CalledProcessError as e:
    print >>sys.stderr, e
    print >>sys.stderr, "Failed to ensure dependencies being up-to-date!"

import buildtools.build

args = sys.argv[:]
if '-t' in args:
    index_opt = args.index('-t')
    index_val = index_opt + 1
    if index_val < len(args):
        args.insert(1, args.pop(index_opt))
        args.insert(2, args.pop(index_val))
buildtools.build.processArgs(BASE_DIR, args)
