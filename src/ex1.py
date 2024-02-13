numbers = [int(n.replace('\n', '')) for n in open('../data/ex1.txt', 'r').readlines()]
print("ans1 = ", sum(numbers))

x = 0
steps = [x]
found = False
while not found:
    for n in numbers:
        x += n
        if x in steps:
            print("ans2 = ", x)
            found = True
            break
        steps.append(x)
        if len(steps) % 10000 == 0:
            print(len(steps), steps[-1])
