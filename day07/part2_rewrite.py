# rewritten to work backwards
# runs just about instantaneously

f = open('day07/input.txt')
txt = [i.strip() for i in f.readlines()]

sum_ = 0

for line in txt:
    test_val, nums = line.split(': ')
    test_val = int(test_val)
    nums = [int(num) for num in nums.split()]
    
    results = [test_val]
    for num in nums[len(nums) - 1:0:-1]:
        new_results = []
        for result in results:
            
            # undo addition
            difference = result - num
            if difference >= nums[0]:
                new_results.append(difference)
                
            # undo multiplication if possible
            if result % num == 0:
                quotient = result // num
                if quotient >= nums[0]:
                    new_results.append(quotient)
                    
            # undo concatenation if possible
            prefix = str(result)[:len(str(result))-len(str(num))]
            prefix = 0 if prefix == '' else int(prefix)     # fix empty int
            if int(str(prefix) + str(num)) == result and prefix >= nums[0]:
                new_results.append(prefix)
                
        results = new_results
        
    if nums[0] in results:
        sum_ += test_val
        
print(sum_)