import os
from datetime import datetime, timedelta
from copy import deepcopy as dc

print(os.getcwd())
lines = [n.replace('\n', '') for n in open('../data/ex4.txt', 'r').readlines()]
sleep_time = dict()
sleep_minute = dict()
start_time = datetime(1, 1, 1)
start_minute = -1
guard = ''
messages = list()
minute_range = {k: 0 for k in range(0, 60)}


for l in lines:
    ts_txt = l.split(']')[0]
    ts_txt = ts_txt[1:]
    ts = datetime.strptime(ts_txt, '%Y-%m-%d %H:%M')
    m = l.split(']')[1]
    messages.append((ts, m))

messages.sort(key=lambda tup: tup[0])


for e in messages:
    t, m = e
    # print(t.strftime('[%Y-%m-%d %H:%M]'), m)
    ix = m.find('#')
    if ix != -1:
        if start_minute != -1:
            print("ERROR at", e)

        guard = ''
        ix += 1
        while m[ix].isnumeric():
            guard += m[ix]
            ix += 1
        if guard not in sleep_minute:
            sleep_minute[guard] = dc(minute_range)
            sleep_time[guard] = timedelta()
    else:
        if 'falls asleep' in m:
            if start_minute != -1:
                print("ERROR at", e)
            start_time = t
            start_minute: int = t.minute
            if t.hour == 23:
                print("ERROR at", e)
        elif 'wakes up' in m:
            if start_minute == -1:
                print("ERROR at", t, m)

            sleep_time[guard] += (t - start_time)
            for mn in range(start_minute, t.minute):
                sleep_minute[guard][mn] += 1
            start_minute = -1

max_time = 0
max_guard = ''
for k, v in sleep_time.items():
    minutes = int(v.total_seconds())/60
    if minutes > max_time:
        max_time = minutes
        max_guard = k

max_minute = max(sleep_minute[max_guard].values())
# print(sleep_minute[max_guard])
for k, v in sleep_minute[max_guard].items():
    # print(f"{k}: {v}")
    if v == max_minute:
        print(f"ans pt 1 = {k * int(max_guard)}")

max_minute = 0
max_times = 0
for guard in sleep_minute.keys():
    for k, v in sleep_minute[guard].items():
        if v > max_times:
            max_times = v
            max_minute = k
            max_guard = guard
print(f"ans pt 2 = {max_minute * int(max_guard)}")

