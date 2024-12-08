f = open('day07/input.txt')
txt = [i.strip() for i in f.readlines()]

sum_ = 0

for line in txt:
    test_val, nums = line.split(': ')
    test_val = int(test_val)
    nums = nums.split()     # list of strings

    ok = False
    
    for n in range(2**(len(nums) - 1)):
        ops = bin(n)[2:].zfill(len(nums) - 1).replace('0', '+').replace('1', '*')

        result = nums[0]
        for i in range(len(ops)):
            result = eval(str(result) + ops[i] + nums[i+1])
            if result > test_val: break     # might help with speed
        
        if result == test_val:
            ok = True
            break
    
    if ok:
        sum_ += test_val

print(sum_)