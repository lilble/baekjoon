# 	31256KB	44ms

# d[n][a] : a로 시작하는 n자리 이친수
n = int(input())
d = [[0]*2 for _ in range(n+1)]
d[1] = [1, 1]
for i in range(2, n+1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]
print(d[n][1])