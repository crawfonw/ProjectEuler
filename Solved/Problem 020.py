def factorial(num):
    total = 1
    for i in range(num):
        total *= (i+1)
    return total

def break_to_digits(num):
    nums = []
    for elem in str(num):
        nums.append(elem)
    for i in nums:
        nums.append(int(nums[0]))
        nums.remove(nums[0])
    return nums

def sum_up(nums):
    total = 0
    for elem in nums:
        total += elem
    return total

print sum_up(break_to_digits(factorial(100)))
