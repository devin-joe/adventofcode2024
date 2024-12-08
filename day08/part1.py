f = open('day08/input.txt')
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
            y1 = 2 * yi - yj
            x1 = 2 * xi - xj
            y2 = 2 * yj - yi
            x2 = 2 * xj - xi
            if y1 >= 0 and y1 < len(map) and x1 >= 0 and x1 < len(map[y1]):
                if map[y1][x1] != '#':
                    map[y1] = map[y1][:x1] + '#' + map[y1][x1+1:]
            if y2 >= 0 and y2 < len(map) and x2 >= 0 and x2 < len(map[y2]):
                if map[y2][x2] != '#':
                    map[y2] = map[y2][:x2] + '#' + map[y2][x2+1:]

print(sum([line.count('#') for line in map]))