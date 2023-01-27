# pypy3 	119688KB	1300ms

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
def calc(c):
    ans = 0
    for x in c:
        for y in c:
            ans += s[x][y]
    return ans
def f(idx, a, b):
    ans = -1
    if idx == n:
        return abs(calc(a) - calc(b))
    if idx > n:
        return -1
    t1 = f(idx+1, a+[idx], b)
    if ans == -1 or t1 < ans:
        ans = t1
    t2 = f(idx+1, a, b+[idx])
    if ans == -1 or t2 < ans:
        ans = t2
    return ans
print(f(0, [], []))