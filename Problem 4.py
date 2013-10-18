import time

def is_palindrome(num):
    '''hardcoded for 5 & 6 digit num'''
    snum = str(num)
    if(len(str(num)) == 5):
        parts = [snum[:2], snum[3:]]
        parts[1] = parts[1][1] + parts[1][0]
    elif(len(str(num)) == 6):
        parts = [snum[:3], snum[3:]]
        parts[1] = parts[1][2] + parts[1][1] + parts[1][0]
    if parts[0] == parts[1]:
        return True
        
    return False

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j) and i*j > largest:
            largest = i*j

t1 = time.time()
print largest
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
