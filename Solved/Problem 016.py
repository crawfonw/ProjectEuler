import time

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

t1 = time.time()
print sum_up(break_to_digits(2**1000))
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
