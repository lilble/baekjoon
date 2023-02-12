# 	31388KB	124ms

t = int(input())
gears = [list(map(int, input())) for _ in range(t)]

def rotate(n, r):
    cur = gears[n]
    if r == 1:
        gears[n] = [cur[-1]] + cur[:-1]
    if r == -1:
        gears[n] = cur[1:] + [cur[0]]

def f(n, r, d):
    cur = gears[n]
    if d == 1:
        if gears[n-1][2] != cur[6]:
            if n < t-1:
                f(n+1, -r, d)
            rotate(n, r)
    if d == -1:
        if gears[n+1][6] != cur[2]:
            if n > 0:
                f(n-1, -r, d)
            rotate(n, r)
            
k = int(input())
for _ in range(k):
    n, r = map(int, input().split())
    n -= 1
    if n < t-1:
        f(n+1, -r, 1)
    if n > 0:
        f(n-1, -r, -1)
    rotate(n, r)
    
ans = 0
for g in gears:
    ans += g[0]
print(ans)