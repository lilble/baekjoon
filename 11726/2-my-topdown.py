# 30616KB	40ms

def f(n):
    if d[n]:
        return d[n]
    d[n] = f(n-1) + f(n-2)
    return d[n]
n = int(input())
d = [0]*(n+2)
d[1] = 1
d[2] = 2
print(f(n)%10007)