#31256KB	44ms

# dynamic programming

# d[n][a] = a로 시작하는 길이가 n인 계단 수 개수.
MOD = 1000000000
n = int(input())
d = [[0]*10 for _ in range(n+1)]
d[1] = [1]*10
for i in range(2, n+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for a in range(1,9):
        d[i][a] = (d[i-1][a-1] + d[i-1][a+1])%MOD
ans = 0
for i in range(1, 10):
    ans += d[n][i]
print(ans%MOD)