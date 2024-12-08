f = open('day03/input.txt')
txt = [i.strip() for i in f.readlines()]

# Watch me cook

text = ' '.join(txt)

sum_ = 0

i = 3
state = 'nothign very special going on'
n1 = 0
n2 = 0
while i < len(text):
    if state == 'dont':
        if text[i-3:i+1] == 'do()':
            state = 'nothign very special going on'
    elif state == 'reading the first number':
        if text[i] == ',':
            state = 'reading the second number'
        elif text[i].isdigit():
            n1 = 10 * n1 + int(text[i])
        else:
            state = 'nothign very special going on'
    elif state == 'reading the second number':
        if text[i] == ')':
            sum_ += n1 * n2
            state = 'nothign very special going on'
        elif text[i].isdigit():
            n2 = 10 * n2 + int(text[i])
        else:
            state = 'nothign very special going on'
    elif text[i-3:i+1] == 'mul(':
        state = 'reading the first number'
        n1 = 0
        n2 = 0
    elif text[i-6:i+1] == "don't()":
        state = 'dont'
    i += 1

print(sum_)