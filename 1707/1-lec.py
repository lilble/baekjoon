# 53344KB	1220ms

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# color[node] = 0(방문x), 1(A쪽), 2(B쪽)
def dfs(node, c): # node에 방문. 색은 c다
    color[node] = c
    for i in a[node]:
        if color[i] == 0:
            if dfs(i, 3-c) == False:
                return False
        elif color[i] == color[node]:
            return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    color = [0]*(v+1)
    for _ in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    ok = 'YES'
    for i in range(1, v+1):
        if color[i] == 0:
            if dfs(i, 1) == False:
                ok = 'NO'
                break
    print(ok)