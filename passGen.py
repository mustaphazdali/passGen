#!/bin/python3
from itertools import product
import sys

words = sys.argv[2:]
l = sys.argv[1]

for i in range(l):
  for p in product(words, repeat=i+1):
    print(''.join(p))
