# 34176KB	1432ms

from collections import deque
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
def f(start, dest):
    q = deque()
    q.append((start[0], start[1]))
    while q:
        x,y = q.popleft()
        if [x, y] == dest:
            return
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<l and 0<=ny<l:
                if d[nx][ny] == 0:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    dest =  list(map(int, input().split()))
    d = [[0]*l for _ in range(l)]
    f(start, dest)
    print(d[dest[0]][dest[1]])