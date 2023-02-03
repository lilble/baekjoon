#	65180KB	724ms

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
def dfs(v):
    check[v] = True
    for i in a[v]:
        if check[i] == False:
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if check[i] == False:
        dfs(i)
        cnt += 1
print(cnt)