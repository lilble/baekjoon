# 30616KB	3720ms

import sys
m = int(input())
s = 0
for _ in range(m):
    c = sys.stdin.readline().split()
    com = c[0]
    if len(c) == 1:
        if com == 'all':
            s = ~0
        elif com == 'empty':
            s = 0
    else:
        num = 1<<(int(c[1])-1)
        if com == 'add':
            s |= num
        elif com == 'remove':
            s &= ~num
        elif com == 'check':
            if s&num > 0:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            s ^= num