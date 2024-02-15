"""
--- Day 5: Alchemical Reduction ---
"""

from string import ascii_lowercase


def reduce(_line):
    cont = True
    while cont:
        cont = False
        for c in ascii_lowercase:
            sub = f"{c}{c.upper()}"
            for _ in range(2):
                new_line = _line.replace(sub, '')
                cont = (new_line != _line) or cont
                _line = new_line
                sub = sub[::-1]
    return _line


line = open('../data/ex5.txt', 'r').read()
print(f"ans pt1 = {len(reduce(line))}")

ans_pt2 = 9999
for c in ascii_lowercase:
    ans_pt2 = min(ans_pt2, len(reduce(line.replace(c, '').replace(c.upper(), ''))))

print(f"ans pt2 = {ans_pt2}")

