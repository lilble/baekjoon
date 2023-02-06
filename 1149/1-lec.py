# 	31396KB	84ms

import sys
sys.setrecursionlimit(1000000)
n = int(input())
cost = []
d = [[-1]*3 for _ in range(n)]
for _ in range(n):
    cost.append(list(map(int, input().split())))
d[0] = cost[0]
def f(h, c):
    colors = [0, 1, 2]
    colors.remove(c)
    if d[h][c] != -1:
        return d[h][c]
    d[h][c] = min(f(h-1, colors[0]), f(h-1, colors[1])) + cost[h][c]
    return d[h][c]
print(min(f(n-1, 0), f(n-1, 1), f(n-1, 2)))