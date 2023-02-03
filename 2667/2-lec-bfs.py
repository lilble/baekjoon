# 31256KB	44ms

n = int(input())
a = []
for _ in range(n):
    a.append(input())
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,c):
    q = []
    q.append((x,y))
    color[x][y] = c
    cnt = 1
    while q:
        (x,y) = q.pop(0)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if a[nx][ny] == '1' and color[nx][ny] == 0:
                    q.append((nx,ny))
                    color[nx][ny] = c
                    cnt += 1
    return cnt
color = [[0]*n for _ in range(n)]
idx = 0
ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == '1' and color[i][j] == 0:
            idx += 1
            ans.append(bfs(i,j,idx))
print(idx)
ans.sort()
for a in ans:
    print(a)