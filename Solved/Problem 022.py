import time

t1 = time.time()
f = open('names.txt','r')
l = f.readline()
f.close()
_list = l.replace('"','').split(',')
_list.sort()

score_sum = 0
for name in _list:
    name_score = 0
    for letter in name:
        if letter == 'A':
            name_score += 1
        elif letter == 'B':
            name_score += 2
        elif letter == 'C':
            name_score += 3
        elif letter == 'D':
            name_score += 4
        elif letter == 'E':
            name_score += 5
        elif letter == 'F':
            name_score += 6
        elif letter == 'G':
            name_score += 7
        elif letter == 'H':
            name_score += 8
        elif letter == 'I':
            name_score += 9
        elif letter == 'J':
            name_score += 10
        elif letter == 'K':
            name_score += 11
        elif letter == 'L':
            name_score += 12
        elif letter == 'M':
            name_score += 13
        elif letter == 'N':
            name_score += 14
        elif letter == 'O':
            name_score += 15
        elif letter == 'P':
            name_score += 16
        elif letter == 'Q':
            name_score += 17
        elif letter == 'R':
            name_score += 18
        elif letter == 'S':
            name_score += 19
        elif letter == 'T':
            name_score += 20
        elif letter == 'U':
            name_score += 21
        elif letter == 'V':
            name_score += 22
        elif letter == 'W':
            name_score += 23
        elif letter == 'X':
            name_score += 24
        elif letter == 'Y':
            name_score += 25
        elif letter == 'Z':
            name_score += 26
    score_sum += name_score * (_list.index(name) + 1)
        
print score_sum
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
