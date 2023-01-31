MAX = 100000
MOD = 1000000009
def f(n, prev):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if d[n][prev] > 0:
        return d[n][prev]
    if prev == 1:
        d[n][1] = f(n-2, 2) + f(n-3, 3)
    elif prev == 2:
        d[n][2] = f(n-1, 1) + f(n-3, 3)
    elif prev == 3:
        d[n][3] = f(n-1, 1) + f(n-2, 2)
    else:
        d[n][0] = f(n-1, 1) + f(n-2, 2) + f(n-3, 3)
    return d[n][prev]
t = int(input())
d = [[0]*4 for _ in range(MAX+1)]
for _ in range(t):
    n = int(input())
    print(f(n, 0)%MOD)