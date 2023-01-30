# 	30616KB	52ms

def f(n):
    if n < 0:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = f(n-1) + f(n-2) + f(n-3)
    return d[n]
t = int(input())
for _ in range(t):
    n = int(input())
    d = [0]*(n+1)
    d[0] = 1
    print(f(n))