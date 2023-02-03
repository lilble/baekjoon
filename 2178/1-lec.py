# 	31256KB	56ms

# dfs로는 해결불가. 최단경로는 bfs로 풀어야 함.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
a = []
n, m = map(int, input().split())
for _ in range(n):
    a.append(list(map(int, input())))
check = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
def bfs():
    q = []
    q.append((0,0))
    check[0][0] = True
    dist[0][0] = 1
    while q:
        (x, y) = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny] == 1 and not check[nx][ny]:
                    q.append((nx,ny))
                    check[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
    return -1
bfs()
print(dist[n-1][m-1])