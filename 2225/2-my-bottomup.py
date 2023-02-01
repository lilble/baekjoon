# 	32276KB	736ms

# d(n, k) = k개 정수 합이 n이 되는 경우의 수
# d(0, x) = 1
MOD = 1000000000
n, k = map(int, input().split())
d = [[0]*(k+1) for _ in range(n+1)]
d[0] = [1]*(k+1)
for i in range(1, n+1):
    for j in range(1, k+1):
        for x in range(i+1):
            d[i][j] += d[x][j-1]
        d[i][j] %= MOD
print(d[n][k])