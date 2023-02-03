# 	39344KB	192ms

MAX = 200000
from collections import deque
n, k = map(int, input().split())
q = deque()
q.append(n)
dist = [-1]*MAX
dist[n] = 0
while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        break
    x = cur*2
    if 0<=x<MAX and dist[x] == -1:
        dist[x] = dist[cur]
        q.appendleft(x)
    for x in [cur+1, cur-1]:
        if 0<=x<MAX and dist[x] == -1:
            dist[x] = dist[cur] + 1
            q.append(x)