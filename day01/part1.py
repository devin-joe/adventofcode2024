f = open('day01/input.txt')
txt = [i.strip() for i in f.readlines()]

L = []
R = []

for line in txt:
    margaret, thatcher = line.split()
    L.append(int(margaret))
    R.append(int(thatcher))

sum_ = 0
for i, j in zip(sorted(L), sorted(R)):
    sum_ += abs(i - j)

print(sum_)