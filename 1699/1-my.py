# pypy3 115112KB	204ms

n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    t = tt = 1
    while i >= tt:
        if d[i] == 0:
            d[i] = d[i-tt]+1
        else:
            d[i] = min(d[i], d[i-tt]+1)
        t += 1
        tt = t**2
print(d[n])