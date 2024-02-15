"""
--- Day 3: No Matter How You Slice It ---
"""
codes = [n.replace('\n', '') for n in open('../data/ex3.txt', 'r').readlines()]
counter = dict()
claims: list[set] = list()
overlapping_claims = set()

for i, c in enumerate(codes):
    rel_part = c.split('@')[1]
    sizes = rel_part.split(':')[1]
    start_points = rel_part.split(':')[0]
    x_start, y_start = start_points.split(',')
    x_size, y_size = sizes.split('x')
    claim = set()

    for x in range(int(x_start), int(x_start) + int(x_size)):
        for y in range(int(y_start), int(y_start) + int(y_size)):
            claim.add((x, y))
            if (x, y) in counter:
                counter[(x, y)] += 1
                overlapping_claims.add(i+1)
            else:
                counter[(x, y)] = 1
    claims.append(claim)
print(f"ans pt 1 = {len(list(filter(lambda k: k > 1, counter.values())))}")

for i, c1 in enumerate(claims):
    if i+1 in overlapping_claims:
        continue
    for j, c2 in enumerate(claims):
        if i+1 == j+1:
            continue
        if len(c1.intersection(c2)) > 0:
            overlapping_claims.add(i+1)
            overlapping_claims.add(j+1)
            break
    if i+1 not in overlapping_claims:
        print(f"ans pt 2 = {i+1}")
        break
