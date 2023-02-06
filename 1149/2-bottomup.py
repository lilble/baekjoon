# 31256KB	80ms

n = int(input())
cost = []
d = [[-1]*3 for _ in range(n)]
for _ in range(n):
    cost.append(list(map(int, input().split())))
d[0] = cost[0]
for h in range(1, n):
    d[h][0] = min(d[h-1][1], d[h-1][2]) + cost[h][0]
    d[h][1] = min(d[h-1][0], d[h-1][2]) + cost[h][1]
    d[h][2] = min(d[h-1][0], d[h-1][1]) + cost[h][2]
print(min(d[n-1][0], d[n-1][1], d[n-1][2]))