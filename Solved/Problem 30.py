import time

nums = []
n = 5
a = 10
b = 295245

t1 = time.time()

for i in range(a, b):
    s = str(i)
    sumpow = sum([int(c)**n for c in s])
    if sumpow == i:
        nums.append(i)

print nums, sum(nums)

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))

