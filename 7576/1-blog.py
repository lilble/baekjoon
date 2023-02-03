# 	98604KB	2384ms

import sys
input = sys.stdin.readline
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      q.append((i,j))
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if a[nx][ny] == 0:
                a[nx][ny] = a[x][y] + 1
                q.append((nx,ny))
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, a[i][j])
print(ans-1)