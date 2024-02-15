"""
--- Day 4: Repose Record ---
"""

import os
from datetime import datetime, timedelta
from copy import deepcopy as dc

print(os.getcwd())
with open('../data/ex4.txt', 'r', encoding='utf-8') as f:
    lines = [n.replace('\n', '') for n in f.readlines()]

sleep_time = {}
sleep_minute = {}
start_time = datetime(1, 1, 1)
start_minute = -1
guard = ''
messages = []
minute_range = {k: 0 for k in range(0, 60)}

for line in lines:
    ts_txt = line.split(']')[0]
    ts_txt = ts_txt[1:]
    ts = datetime.strptime(ts_txt, '%Y-%m-%d %H:%M')
    m = line.split(']')[1]
    messages.append((ts, m))

messages.sort(key=lambda tup: tup[0])


for e in messages:
    t, m = e
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

MAX_TIME = 0
MAX_GUARD = ''
for k, v in sleep_time.items():
    minutes = int(v.total_seconds())/60
    if minutes > MAX_TIME:
        MAX_TIME = minutes
        MAX_GUARD = k

MAX_MINUTE = max(sleep_minute[MAX_GUARD].values())
for k, v in sleep_minute[MAX_GUARD].items():
    if v == MAX_MINUTE:
        print(f"ans pt 1 = {k * int(MAX_GUARD)}")

MAX_MINUTE = 0
MAX_TIMES = 0
for guard in sleep_minute.keys():
    for k, v in sleep_minute[guard].items():
        if v > MAX_TIMES:
            MAX_TIMES = v
            MAX_MINUTE = k
            MAX_GUARD = MAX_GUARD
print(f"ans pt 2 = {MAX_MINUTE * int(MAX_GUARD)}")

