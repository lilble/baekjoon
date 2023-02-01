# 	31256KB	48ms

# top-down

NO = -15*1000
n = int(input())
t = []
p = []
d = [0]*(n+1)
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)
def f(idx):
    if idx > n:
        return NO
    if idx == n:
        return 0
    if d[idx] > 0:
        return d[idx]
    return max(f(idx+1), f(idx+t[idx]) + p[idx])
print(f(0))