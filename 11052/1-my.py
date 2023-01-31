# 	31256KB	188ms

# Top-Down

def f(n):
    if d[n] > 0:
        return d[n]
    d[n] = p[n-1]
    for i in range(1,n):
        d[n] = max(d[n], p[n-1-i]+f(i))
    return d[n]
n = int(input())
p = list(map(int,input().split()))
d = [0]*(n+1)
print(f(n))