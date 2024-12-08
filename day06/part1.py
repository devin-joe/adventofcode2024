f = open('day06/input.txt')
txt = [i.strip() for i in f.readlines()]

map = txt
for r in range(len(map)):
    if '^' in map[r]:
        y = r
        x = map[r].index('^')

v = [-1, 0]

while y + v[0] >= 0 and y + v[0] < len(map) and x + v[1] >= 0 and x + v[1] < len(map[0]):
    if map[y+v[0]][x+v[1]] == '#':
        v = [v[1], -v[0]] # turn right
    else:
        map[y] = map[y][:x] + 'X' + map[y][x+1:]
        y += v[0]
        x += v[1]
map[y] = map[y][:x] + 'X' + map[y][x+1:]

print(sum([i.count('X') for i in map]))