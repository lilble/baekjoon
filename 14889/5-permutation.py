# pypy3: 115360KB	564ms
# python3: 30748KB	6020ms

# using permutation

def calc(a, s):
    ans = 0
    for x in a:
        for y in a:
            ans += s[x][y]
    return ans
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
m = 10000
for i in range(1, 1<<n):
    cnt = 0
    a = []
    b = []
    for k in range(n):
        if i&(1<<k):
            cnt += 1
            a.append(k)
        else:
            b.append(k)
    if cnt == n//2:
        m = min(m, abs(calc(a, s)-calc(b, s)))
print(m)