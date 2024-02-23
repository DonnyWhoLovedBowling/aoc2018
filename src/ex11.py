"""
--- Day 11: Chronal Charge ---
"""

powers = {}
serial_number = 2694
# serial_number = 18
# serial_number = 42
max_range = 300
lookup = {}


def calc_power_grid(_x, _y, _size):
    global lookup
    if (_x, _y, _size-1) in lookup:
        total_power = lookup[(_x, _y, _size-1)]
        x = (_x + _size) - 1
        for y in range(_y, (_y + _size) - 1):
            total_power += powers[(x, y)]
        y = (_y + _size) - 1
        for x in range(_x, (_x + _size)):
            total_power += powers[(x, y)]
    elif (_x-1, _y, _size) in lookup:
        total_power = lookup[(_x-1, _y, _size)]
        for y in range(_y, (_y + _size)):
            total_power -= powers[(_x - 1, y)]
            total_power += powers[((_x + _size) - 1, y)]
    elif (_x, _y-1, _size) in lookup:
        total_power = lookup[(_x, _y - 1, _size)]
        for x in range(_x, (_x + _size)):
            total_power -= powers[(x, _y - 1)]
            total_power += powers[(x, (_y + _size) - 1)]
    else:
        total_power = 0
        for i in range(0, _size):
            for j in range(0, _size):
                key = (_x+i, _y+j)
                if key in powers:
                    total_power += powers[key]

    lookup[_x, _y, _size] = total_power
    return total_power


def calcpowers():
    global powers
    for x in range(1, max_range+1):
        for y in range(1, max_range+1):
            rack_id = x+10
            power_level = rack_id*y
            power_level += serial_number
            power_level *= rack_id
            if power_level > 100:
                power_level = int(str(power_level)[-3])
            else:
                power_level = 0
            power_level -= 5
            powers[(x, y)] = power_level


def run(pt):
    max_power = 0
    max_coor = 0

    for size in range(1, max_range + 1):
        if pt == 1 and size != 3:
            continue
        for x in range(1, (max_range-size)+1):
            for y in range(1, (max_range-size)+1):
                power = calc_power_grid(x, y, size)
                if power > max_power:
                    max_power = power
                    max_coor = (x, y, size)
    if pt == 1:
        print(f"ans pt {pt}: {max_coor[0]},{max_coor[1]}")
    else:
        print(f"ans pt {pt}: {max_coor[0]},{max_coor[1]},{max_coor[2]}")


if '__main__' == __name__:
    calcpowers()
    run(1)
    run(2)
