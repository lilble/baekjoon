# 30616KB	44ms

n = int(input())
t = []
p = []
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)
def f(idx, s):
    if idx >= n:
        return s
    ni = idx+t[idx]
    skip = f(idx+1, s)
    if ni <= n:
        return max(skip, f(ni, s+p[idx]))
    else:
        return max(skip, s)
    
print(f(0, 0))