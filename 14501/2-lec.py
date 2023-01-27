# 30616KB	68ms

n = int(input())
t = []
p = []
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)
ans = 0
def f(idx, s):
    global ans
    if idx > n:
        return
    if idx == n:
        ans = max(ans, s)
        return
    f(idx+1, s)
    f(idx+t[idx], s+p[idx])
f(0, 0)
print(ans)