# 	34160KB	88ms

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input())))
c = [[-1]*m for _ in range(n)]
c[0][0] = 0
q = deque()
q.append((0,0))
while q:
    x, y = q.popleft()
    if (x, y) == (n-1, m-1):
        print(c[x][y])
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if c[nx][ny] == -1:
                if a[nx][ny] == 1:
                    c[nx][ny] = c[x][y] + 1
                    q.append((nx,ny))
                else:
                    c[nx][ny] = c[x][y]
                    q.appendleft((nx,ny))