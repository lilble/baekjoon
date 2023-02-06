# Recursion error (limit 초과인듯)

MOD = 1000000009
MAX = 1000000
d = [0]*(MAX+1) 
d[0] = 1
def f(n):
    if n < 0:
        return 0
    if d[n] != 0:
        return d[n]
    d[n] = f(n-1) + f(n-2) + f(n-3)
    return d[n]
t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n)%MOD)