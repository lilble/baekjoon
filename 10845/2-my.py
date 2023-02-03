# python3: 31256KB	76ms

import sys
q = []
n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop(0))
        if command[0] == 'size':
            print(len(q))
        if command[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        if command[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        if command[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
    else:
        q.append(int(command[1]))