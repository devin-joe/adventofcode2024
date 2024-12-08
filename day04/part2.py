f = open('day04/input.txt')
txt = [i.strip() for i in f.readlines()]

width = len(txt[0])
height = len(txt)

sum_ = 0

for r in range(1, height - 1):
    for c in range(1, width - 1):
        if txt[r][c] == 'A':
            hugeconditionwhichirefusetoshorteninanyway = (txt[r-1][c-1] == 'M' and txt[r+1][c+1] == 'S' or txt[r-1][c-1] == 'S' and txt[r+1][c+1] == 'M') and ( txt[r-1][c+1] == 'M' and txt[r+1][c-1] == 'S' or txt[r-1][c+1] == 'S' and txt[r+1][c-1] == 'M')
            if hugeconditionwhichirefusetoshorteninanyway:
                sum_ += 1

print(sum_)