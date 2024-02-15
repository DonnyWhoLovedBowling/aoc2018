import string
from dataclasses import dataclass


@dataclass
class Worker:
    letter: str

    def __post_init__(self):
        self.time_to_finish = 60 + string.ascii_lowercase.index('b')

    def run(self):
        if self.time_to_finish == 1:
            return self.letter
        else:
            self.time_to_finish -= 1
            return ''



lines = [n.replace('\n', '') for n in open('../data/ex7.txt', 'r').readlines()]

req_dict = dict()
enables_dict = dict()
all_nodes = set()


def new_options(enabler):
    ret = []
    global enables_dict, req_dict, ans_list
    if enabler in enables_dict:
        for o in enables_dict[enabler]:
            if o in req_dict.keys():
                reqs = set(req_dict[o])
                if len(reqs.difference(set(ans_list))) == 0:
                    ret.append(o)
            else:
                ret.append(o)
    return ret


for line in lines:
    e = line[5]
    req = line[36]
    all_nodes.add(e)
    all_nodes.add(req)
    if req in req_dict:
        req_dict[req].append(e)
    else:
        req_dict[req] = [e]
    if e in enables_dict:
        enables_dict[e].append(req)
    else:
        enables_dict[e] = [req]

ans_list = []
total_time = 0


def run(pt2=False):
    options = sorted(list(all_nodes.difference(set(req_dict.keys()))), reverse=True)

    global ans_list, total_time
    worker_list = []
    while options:
        new = options.pop()
        if pt2:
            new_options = []
            for w in worker_list:
                new_options.append(w.run())
            worker_list.append(Worker(new))
            total_time += 1
        else:
            ans_list.append(new)
            options += new_options(new)
            options = sorted(options, reverse=True)
        

run()
ans_pt1 = ''.join(ans_list)
print(f"ans pt1 = {ans_pt1}")
