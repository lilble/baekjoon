# 	31256KB	336ms

t = int(input())
gears = [list(map(int, input())) for _ in range(t)]

k = int(input())
for _ in range(k):
    d = [0]*t
    n, r = map(int, input().split())
    n -= 1
    d[n] = r
    for i in range(n-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    for i in range(n+1, t):
        if gears[i-1][2] != gears[i][6]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(t):
        cur = gears[i]
        if d[i] == 1:
            gears[i] = [cur[-1]] + cur[:-1]
        elif d[i] == -1:
            gears[i] = cur[1:] + [cur[0]]
    
ans = 0
for g in gears:
    ans += g[0]
print(ans)