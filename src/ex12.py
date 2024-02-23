"""
--- Day 12: Subterranean Sustainability ---
"""

from copy import deepcopy as dc


def calc_score(_pots, _ref):
    score = 0
    for i, p in enumerate(_pots):
        if p == '#':
            score += i - ref
    return score


lines = [line.replace('\n', '') for line in open('../data/ex12.txt').readlines()]
pots = list(lines[0].split(":")[1].strip())
patterns = [line.split(' => ')[0] for line in lines if '=>' in line and line.split(' => ')[1].strip() == '#']
print(patterns)
prefix = ['.']*5
suffix = ['.']*5
pots = prefix + pots + suffix
ref = ''.join(pots).find('#')
last_score = calc_score(pots, ref)
# print(last_score, ''.join(pots))
ans_pt_1 = 0
for _ in range(20):
    new_pots = dc(pots)
    for p in range(len(pots)-4):
        test = ''.join(pots[p:p+5])
        if test in patterns:
            new_pots[p+2] = '#'
        else:
            new_pots[p+2] = '.'
    if new_pots[-3] == '#':
        new_pots += ['.', '.']
    pots = dc(new_pots)
    new_score = calc_score(pots, ref)
    print(new_score, ''.join(pots))
    if _ == 19:
        ans_pt_1 = new_score

print(f"ans pt1 = {ans_pt_1}")
print(f"ans pt2 = {50000000000*80}")


