f = open('day01/input.txt')
txt = [i.strip() for i in f.readlines()]

L = []
R = []

for line in txt:
    margaret, thatcher = line.split()
    L.append(int(margaret))
    R.append(int(thatcher))

sum_ = 0
for n in L:
    sum_ += n * R.count(n)

print(sum_)