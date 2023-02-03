# python3:	31388KB	52ms

import sys
d = []
n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == 'pop_front':
            if len(d) == 0:
                print(-1)
            else:
                print(d.pop(0))
        if command[0] == 'pop_back':
            if len(d) == 0:
                print(-1)
            else:
                print(d.pop())
        if command[0] == 'size':
            print(len(d))
        if command[0] == 'empty':
            if len(d) == 0:
                print(1)
            else:
                print(0)
        if command[0] == 'front':
            if len(d) == 0:
                print(-1)
            else:
                print(d[0])
        if command[0] == 'back':
            if len(d) == 0:
                print(-1)
            else:
                print(d[-1])
    else:
        num = int(command[1])
        if command[0] == 'push_front':
            d.insert(0, num)
        if command[0] == 'push_back':
            d.append(num)