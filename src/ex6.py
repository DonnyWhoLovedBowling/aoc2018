"""
--- Day 6: Chronal Coordinates ---
"""
lines = [n.replace('\n', '') for n in open('../data/ex6.txt', 'r').readlines()]

xs = [int(line.split(', ')[0]) for line in lines]
ys = [int(line.split(', ')[1]) for line in lines]

x_min, x_max = min(xs), max(xs)
y_min, y_max = min(ys), max(ys)


dist_map = dict()
edges = set()
ans_pt2 = 0
ans_list = 0

for x in range(x_min-1, x_max+1):
    for y in range(y_min - 1, y_max + 1):
        min_dist = 99999
        min_i = -1
        total_dist = 0
        for i in range(len(xs)):
            dist = abs(x-xs[i])+abs(y-ys[i])
            total_dist += dist
            if dist < min_dist:
                min_i = i
                min_dist = dist
            elif dist == min_dist:
                min_i = -1
        if total_dist < 10000:
            ans_pt2 += 1
        if min_i != -1:
            dist_map[(x, y)] = min_i
            if x == x_max or x == x_min-1 or y == y_min-1 or y == y_max:
                edges.add(min_i)

for k, v in dist_map.items():
    if v in edges:
        pass
    else:
        ans_list += 1

print(f"ans pt1 = {ans_list}")
print(f"ans pt2 = {ans_pt2}")

