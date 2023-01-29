# 	30748KB	868ms

n, m = map(int, input().split())
p = [list(map(int, input())) for _ in range(n)]
ans = 0
# 0:-, 1:|
for b in range(1<<(n*m)):
    s = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if b&(1<<k) == 0:
                cur = cur*10 + p[i][j]
            else:
                s += cur
                cur = 0
        s += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if b&(1<<k) != 0:
                cur = cur*10 + p[i][j]
            else:
                s += cur
                cur = 0
        s += cur
    ans = max(s, ans)
print(ans)