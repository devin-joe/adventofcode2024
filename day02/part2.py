f = open('day02/input.txt')
txt = [i.strip() for i in f.readlines()]

sum_ = 0

for line in txt:
    report = [int(i) for i in line.split()]
    ok = False
    for margaret in range(len(report)):
        deport = report[:margaret] + report[margaret + 1:]
        diffs = [deport[i + 1] - deport[i] for i in range(len(deport) - 1)]
        if all(i >= 1 and i <= 3 for i in diffs) or all(i >= -3 and i <= -1 for i in diffs):
            ok = True
    if ok:
        sum_ += 1

print(sum_)