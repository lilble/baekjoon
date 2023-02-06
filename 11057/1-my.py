# 31256KB	60ms

# d(n, i) = n번째 수가 i일때 오르막수 개수
MOD = 10007
l = int(input())
d = [[0]*10 for _ in range(l)]
d[0] = [1]*10
for n in range(1, l):
    for i in range(10):
        for j in range(i+1):
            d[n][i] += d[n-1][j]
        d[n][i] %= MOD
print(sum(d[l-1])%MOD)