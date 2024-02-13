from datetime import datetime, timedelta

lines = [n.replace('\n', '') for n in open('../data/ex4.txt', 'r').readlines()]
sleep_time = dict()
start_time = datetime(1,1,1)
guard = ''
messages = list()


for l in lines:
    ts_txt = l.split(']')[0]
    ts_txt = ts_txt[1:]
    ts = datetime.strptime(ts_txt, '%Y-%m-%d %H:%M')
    m = l.split(']')[1]
    messages.append((ts, m))

messages.sort(key=lambda tup: tup[0])

for e in messages:
    t, m = e
    ix = m.find('#')
    if ix != -1:
        guard = ''
        ix += 1
        while m[ix].isnumeric():
            guard += m[ix]
            ix += 1

        if guard not in sleep_time:
            sleep_time[guard] = timedelta()
    else:
        if 'falls asleep' in m:
            start_time = t
        elif 'wakes up' in m:
            sleep_time[guard] += (t - start_time)

max_time = 0
max_guard = 0
print(sleep_time)
for k, v in sleep_time.items():
    minutes = int(v.total_seconds())/60
    if minutes > max_time:
        max_time = minutes
        max_guard = int(k)

print(max_time, max_guard)
print(f"ans pt1 = {max_guard*max_time}")
