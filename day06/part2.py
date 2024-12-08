f = open('day06/input.txt')
txt = [i.strip() for i in f.readlines()]

map = txt
for r in range(len(map)):
    if '^' in map[r]:
        y0 = r
        x0 = map[r].index('^')

y = y0
x = x0
v = [-1, 0]

sum_ = 0
po = 0
tested = [[y0, x0]]

while y + v[0] >= 0 and y + v[0] < len(map) and x + v[1] >= 0 and x + v[1] < len(map[0]):
    if map[y+v[0]][x+v[1]] == '#':
        v = [v[1], -v[0]]
    else:
        y += v[0]
        x += v[1]
    yy, xx = y + v[0], x + v[1] # set obstacle position
    y1, x1, v01, v11 = y, x, v[0], v[1] # set spawn point
    poses = []
    if [yy, xx] not in tested:
        while y + v[0] >= 0 and y + v[0] < len(map) and x + v[1] >= 0 and x + v[1] < len(map[0]):
            if map[y+v[0]][x+v[1]] == '#' or (y+v[0] == yy and x+v[1] == xx):
                v = [v[1], -v[0]]
                if [y, x, v[0], v[1]] in poses:
                    sum_ += 1
                    break
                poses.append([y, x, v[0], v[1]])
            else:
                y += v[0]
                x += v[1]
        y, x = y1, x1
        v = [v01, v11]
    tested.append([yy, xx])
    po += 1

print(sum_)