f = open('day04/input.txt')
txt = [i.strip() for i in f.readlines()]

width = len(txt[0])
height = len(txt)

sum_ = 0

for line in txt:
    sum_ += line.count('XMAS') + line.count('SAMX')

for c in range(width):
    col = ''.join(txt[r][c] for r in range(height))
    sum_ += col.count('XMAS') + col.count('SAMX')

for c in range(width * 2 - 1):
    col = ''.join(('.' * r + txt[r] + '.' * (width - r - 1))[c] for r in range(height))
    sum_ += col.count('XMAS') + col.count('SAMX')

# for r in range(height):
#     print('.' * (width - r - 1) + txt[r] + '.' * r)

for c in range(width * 2 - 1):
    col = ''.join(('.' * (width - r - 1) + txt[r] + '.' * r)[c] for r in range(height))
    sum_ += col.count('XMAS') + col.count('SAMX')

print(sum_)