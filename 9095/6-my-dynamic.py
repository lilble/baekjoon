#	30616KB	36ms

def f(n):
    if d[n] > 0:
        return d[n]
    d[n] = f(n-1) + f(n-2) + f(n-3)
    return d[n]
t = int(input())
for _ in range(t):
    n = int(input())
    d = [0]*(n+3)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    print(f(n))