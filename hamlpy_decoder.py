#! /usr/bin/env python3

from __future__ import print_function

import sys
from hamlpy.compiler import Compiler

with open(sys.argv[1]) as f:
    haml = f.read()

compiler = Compiler()
html = compiler.process(haml)

print(html)
