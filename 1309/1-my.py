# 50468KB	164ms

# d(i, j) = i행 j칸에 사자있을 때 0~i행까지의 방법 수
MOD = 9901
n = int(input())
d = [[0]*3 for _ in range(n)]
d[0] = [1, 1, 1]
for i in range(1, n):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2])%MOD
    d[i][1] = (d[i-1][0] + d[i-1][2])%MOD
    d[i][2] = (d[i-1][0] + d[i-1][1])%MOD
print((d[n-1][0] + d[n-1][1] + d[n-1][2])%MOD)