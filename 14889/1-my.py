#30616KB	1972ms
# recursive, but uses global var

def status(c):
    ans = 0
    for x in c:
        for y in c:
            ans += s[x][y]
    return ans
def f(idx, a, b):
    global diff
    if idx == n:
        diff = min(diff, abs(status(a)-status(b)))
        return
    if len(a) < half:
        a.append(idx)
        f(idx+1, a, b)
        a.pop()
    if len(b) < half:
        b.append(idx)
        f(idx+1, a, b)
        b.pop()
n = int(input())
half = n//2
s = [list(map(int, input().split())) for _ in range(n)]
diff = 4500
f(0, [], [])
print(diff)