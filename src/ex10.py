import re


def print_positions(_positions, _x_min, _x_max, _y_min, _y_max):
    for y in range(_y_min, _y_max+1):
        line_str = ''
        for x in range(_x_min, _x_max+1):
            if (x, y) in _positions:
                line_str += '#'
            else:
                line_str += '.'
        print(line_str)


lines = open("../data/ex10.txt").readlines()
positions = []
velocities = []
margin = 500
for line in lines:
    print(line)
    nums = [int(d) for d in re.findall(r'-?\d+', line)]
    print(nums)
    positions.append((int(nums[0]), int(nums[1])))
    velocities.append((int(nums[2]), int(nums[3])))
print(positions)
do_break = False
for s in range(15000):
    if s % 1000 == 0:
        print(f"second {s}")
    min_x, max_x, min_y, max_y = 50000, -50000, 50000, -50000

    for i in range(len(positions)):
        x_new = positions[i][0] + velocities[i][0]
        y_new = positions[i][1] + velocities[i][1]
        max_x = max(max_x, x_new)
        min_x = min(min_x, x_new)
        max_y = max(max_y, y_new)
        min_y = min(min_y, y_new)
        positions[i] = (x_new, y_new)
    if s == 10000:
        print(min_x, max_x, min_y, max_y)
    if (max_x-min_x) < 100 and (max_y-min_y) < 100:
        print_positions(positions, min_x, max_x, min_y, max_y)
        print(f"#seconds: {s}")
        # do_break = True
        # break
