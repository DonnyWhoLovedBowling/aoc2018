"""
--- Day 8: Memory Maneuver ---
"""

import faulthandler


def parse_node(start_ix, rec_depth=0):
    global total_meta, line
    n_children = line[start_ix]
    n_meta = line[start_ix+1]
    node_length = 0
    inc = 0
    child_node_ix = start_ix + 2 + inc
    values = []
    for child in range(n_children):
        inc, this_value = parse_node(child_node_ix, rec_depth+1)
        values.append(this_value)
        node_length += inc
        child_node_ix += inc
    node_length += (2 + n_meta)
    metas = line[0:start_ix+node_length][-n_meta:]
    value = 0
    if n_children == 0:
        value = sum(metas)
    else:
        for m in metas:
            if len(values) >= m:
                value += values[m-1]
    total_meta += sum(metas)
    return node_length, value


def run():
    faulthandler.enable()
    total_length, total_value = parse_node(0)
    print(f"ans pt1 = {total_meta}")
    print(f"ans pt2 = {total_value}")


if __name__ == '__main__':
    line = [int(c) for c in open('../data/ex8.txt', 'r').read().replace('\n', '').split(' ')]
    total_meta = 0
    run()
