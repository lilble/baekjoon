# 	35276KB	152ms

from collections import deque
MAX = 100000
n, k = map(int, input().split())
time = [-1]*(MAX+1)
q = deque()
q.append(n)
time[n] = 0
while q:
    cur = q.popleft()
    if cur == k:
        print(time[cur])
        exit()
    for x in [cur+1, cur-1, cur*2]:
        if 0 <= x <= MAX and time[x] == -1:
            q.append(x)
            time[x] = time[cur] + 1