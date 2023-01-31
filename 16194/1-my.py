# 	31256	188ms

def f(num):
    if d[num]>0:
        return d[num]
    d[num] = p[num-1]
    for i in range(1,num):
        d[num] = min(d[num], p[num-1-i]+f(i))
    return d[num]
n = int(input())
p = list(map(int, input().split()))
d = [0]*(n+1)
print(f(n))