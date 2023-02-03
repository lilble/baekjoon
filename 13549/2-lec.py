# 큐 2개 이용하기 (현재 큐, 다음 큐)

# 	37936KB	220ms

MAX = 200000
from collections import deque
n, k = map(int, input().split())
q1 = deque()
q2 = deque()
q1.append(n)
dist = [-1]*MAX
dist[n] = 0
while q1:
    cur = q1.popleft()
    if cur == k:
        print(dist[cur])
        break
    x = cur*2
    if 0<=x<MAX and dist[x] == -1:
        dist[x] = dist[cur]
        q1.appendleft(x)
    for x in [cur+1, cur-1]:
        if 0<=x<MAX and dist[x] == -1:
            dist[x] = dist[cur] + 1
            q2.append(x)
    if not q1:
        q1 = q2
        q2 = deque()