f = open('day05/input.txt')
txt = [i.strip() for i in f.readlines()]

rules = []
updates = []

i = 0
while txt[i] != '':
    rules.append([int(i) for i in txt[i].split('|')])
    i += 1

i += 1
while i < len(txt):
    updates.append([int(i) for i in txt[i].split(',')])
    i += 1

sum_ = 0

for u in updates:
    ok = True
    for r in rules:
        if r[0] in u and r[1] in u:
            if u.index(r[0]) > u.index(r[1]):
                ok = False
    if ok:
        sum_ += u[len(u)//2]

print(sum_)
