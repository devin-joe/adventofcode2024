f = open('day08/sample.txt')
txt = [i.strip() for i in f.readlines()]

map = []
for line in txt:
    map.append('.' * len(line))

for c in '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
    nodes = []
    for y in range(len(txt)):
        for x in range(len(txt[y])):
            if txt[y][x] == c:
                nodes.append([y, x])
    # loop through unordered combinations of i and j <= the number of nodes
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i >= j:
                continue
            yi, xi = nodes[i]
            yj, xj = nodes[j]
            dy = yj - yi
            dx = xj - xi
            y, x = yi, xi
            while y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
                if map[y][x] != '#':
                    map[y] = map[y][:x] + '#' + map[y][x+1:]
                y += dy
                x += dx
            y, x = yi - dy, xi - dx
            while y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
                if map[y][x] != '#':
                    map[y] = map[y][:x] + '#' + map[y][x+1:]
                y -= dy
                x -= dx

print(sum([line.count('#') for line in map]))