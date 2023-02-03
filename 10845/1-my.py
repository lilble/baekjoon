# pypy3:  117384KB 180ms
# pyhthon3: 31256KB	52ms

import sys
q = [-1]*10000
front = 0
back = 0
n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == 'pop':
            if front == back:
                print(-1)
            else:
                print(q[front])
                q[front] = -1
                front += 1
        if command[0] == 'size':
            print(back - front)
        if command[0] == 'empty':
            if front == back:
                print(1)
            else:
                print(0)
        if command[0] == 'front':
            print(q[front])
        if command[0] == 'back':
            print(q[back-1])
    else: # push
        q[back] = int(command[1])
        back += 1