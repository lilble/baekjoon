# 126340KB	304ms

MAX = 100000
MOD = 1000000009
d = [[0]*4 for _ in range(MAX+1)]
d[1] = [0, 1, 0, 0]
d[2] = [0, 0, 1, 0]
d[3] = [0, 1, 1, 1]
for i in range(4, MAX+1):
    d[i][1] = (d[i-1][2] + d[i-1][3])%MOD
    d[i][2] = (d[i-2][1] + d[i-2][3])%MOD
    d[i][3] = (d[i-3][1] + d[i-3][2])%MOD
t = int(input())
for _ in range(t):
    n = int(input())
    print((d[n][1]+d[n][2]+d[n][3])%MOD)