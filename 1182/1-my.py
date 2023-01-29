# 30616KB	356ms

def f(idx, add):
    global ans, empty
    if add == s and not empty:
        ans += 1
    empty = False
    for i in range(idx, n):
        f(i+1, add+a[i])
n, s = map(int, input().split())
a = list(map(int, input().split()))
empty = True
ans = 0
f(0, 0)
print(ans)