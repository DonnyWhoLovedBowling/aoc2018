import string


class Worker:
    global all_nodes

    def __init__(self, letter: str):
        self.letter = letter
        base = 60 if len(all_nodes) > 6 else 0
        self.time_to_finish = base + string.ascii_lowercase.index(letter.lower()) + 1

    def run(self):
        if self.time_to_finish == 1:
            self.time_to_finish = 0
            return self.letter
        else:
            self.time_to_finish -= 1
            return None


lines = [n.replace('\n', '') for n in open('../data/ex7.txt', 'r').readlines()]

req_dict = dict()
enables_dict = dict()
all_nodes = set()


def calc_options(enabler):
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

if len(all_nodes) == 6:
    max_workers = 2
else:
    max_workers = 5


def run(pt2=False):
    options = sorted(list(all_nodes.difference(set(req_dict.keys()))), reverse=True)
    global ans_list, total_time, max_workers
    worker_list = []
    while len(ans_list) < len(all_nodes):
        if pt2:
            new_options = []
            new_workers = []
            for w in worker_list:
                n = w.run()
                if n is not None:
                    ans_list.append(n)
                    new_options += calc_options(n)
                else:
                    new_workers.append(w)
            worker_list = new_workers
            options += new_options
            options.sort(reverse=True)
            while len(worker_list) < max_workers and options:
                worker_list.append(Worker(options.pop()))
            if len(ans_list) < len(all_nodes):
                total_time += 1
        else:
            new = options.pop()
            ans_list.append(new)
            options += calc_options(new)
            options.sort(reverse=True)
        

run()
ans_pt1 = ''.join(ans_list)
print(f"ans pt1 = {ans_pt1}")
ans_list = []
run(True)
print(''.join(ans_list))
print(f"ans pt2 = {total_time}")
