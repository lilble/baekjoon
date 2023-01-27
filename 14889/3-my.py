#30616KB	2056ms
# Recursive function returns the answer 

def status(c):
    ans = 0
    for x in c:
        for y in c:
            ans += s[x][y]
    return ans
def f(idx, a, b):
    if idx == n:
        return abs(status(a)-status(b))
    diff = 4500
    if len(a) < half:
        a.append(idx)
        diff = min(diff, f(idx+1, a, b))
        a.pop()
    if len(b) < half:
        b.append(idx)
        diff = min(diff, f(idx+1, a, b))
        b.pop()
    return diff
n = int(input())
half = n//2
s = [list(map(int, input().split())) for _ in range(n)]
print(f(0, [], []))