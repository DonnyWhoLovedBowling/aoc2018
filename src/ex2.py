"""
--- Day 2: Inventory Management System ---
"""
from collections import Counter
import difflib

codes = [n.replace('\n', '') for n in open('../data/ex2.txt', 'r').readlines()]
twos = 0
threes = 0
for c in codes:
    vs = Counter(c).values()
    twos += 1 if 2 in vs else 0
    threes += 1 if 3 in vs else 0

print(twos*threes)
stop = False
for c1 in codes:
    for c2 in codes:
        if c1 == c2:
            continue
        diffs = [x for x in list(difflib.ndiff(c1, c2)) if '+' in x or '-' in x]

        if len(diffs) == 2:
            print(diffs)
            print(c1)

