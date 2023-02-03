# 62816KB	156ms

from collections import deque
s = int(input())
d = [[-1]*2000 for _ in range(2000)]
q = deque()
q.append((1,0))
d[1][0] = 0
while q:
    cur, clip = q.popleft()
    if cur == s:
        print(d[cur][clip])
        break
    if d[cur][cur] == -1:
        d[cur][cur] = d[cur][clip] + 1
        q.append((cur,cur))
    if clip != 0:
        x = cur + clip
        if x < 2000 and d[x][clip] == -1:
            d[x][clip] = d[cur][clip] + 1
            q.append((x,clip))
    x = cur - 1
    if x >= 2 and d[x][clip] == -1:
        d[x][clip] = d[cur][clip] + 1
        q.append((x,clip))