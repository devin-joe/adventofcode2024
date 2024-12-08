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
    relevant_rules = ' '.join([str(i[0]) + '|' + str(i[1]) if i[0] in u and i[1] in u else '' for i in rules])
    u_sorted = sorted(u, key=lambda x: relevant_rules.count('|' + str(x)))
    if u != u_sorted:
        sum_ += u_sorted[len(u_sorted)//2]

print(sum_)