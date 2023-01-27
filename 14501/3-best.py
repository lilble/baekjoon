n = int(input())
t = []
p = []
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)
def f(idx, s):
    if idx > n:
        return 0
    if idx == n:
        return s
    return max(f(idx+1, s), f(idx+t[idx], s+p[idx]))
print(f(0, 0))