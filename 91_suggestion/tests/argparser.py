#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], default=1, help="increase output verbosity")
parser.add_argument('x', type=int, help="display a square of a given number")
args = parser.parse_args()
if args.x:
    answer = args.x **2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.x, answer))
if args.verbosity == 1:
    print("{}^2 == {}".format(args.x, answer))
else:
    print(answer)