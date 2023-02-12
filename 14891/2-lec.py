# 	31256KB	52ms

gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
    d = [0]*4
    n, r = map(int, input().split())
    n -= 1
    d[n] = r
    for i in range(n-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    for i in range(n+1, 4):
        if gears[i][6] != gears[i-1][2]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(4):
        cur = gears[i]
        if d[i] == 1:
            gears[i] = [cur[-1]] + cur[:-1]
        elif d[i] == -1:
            gears[i] = cur[1:] + [cur[0]]
ans = 0
for i in range(4):
    ans += gears[i][0]*(2**i)
print(ans)