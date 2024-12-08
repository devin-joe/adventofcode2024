f = open('day07/input.txt')
txt = [i.strip() for i in f.readlines()]

sum_ = 0

for line in txt:
    test_val, nums = line.split(': ')
    test_val = int(test_val)
    nums = [int(num) for num in nums.split()]
    
    results = [nums[0]]
    for num in nums[1:]:
        new_results = []
        for result in results:
            for op in ['+', '*', '']:
                new_result = eval(str(result) + op + str(num))
                if new_result <= test_val:
                    new_results.append(new_result)
        results = new_results
    
    # print(txt.index(line))
    
    if test_val in results:
        sum_ += test_val

print(sum_)