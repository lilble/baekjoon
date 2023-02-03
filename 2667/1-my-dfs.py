# 	31364KB	44ms

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
a = []
check = [[False]*n for _ in range(n)]
for _ in range(n):
    t = input()
    a.append(t)

def dfs(x,y,c):
    cnt = 1
    color[x][y] = c
    check[x][y] = True
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if a[nx][ny] == '1' and not check[nx][ny]:
                cnt += dfs(nx,ny,c)
    return cnt
    
color = [[0]*n for _ in range(n)]
idx = 0
ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == '1' and color[i][j] == 0:
            idx += 1
            ans.append(dfs(i,j,idx))
print(idx)
ans.sort()
for x in ans:
    print(x)