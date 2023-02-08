# 	33300KB	440ms

# d[i][j] = i번째 포도주가 j번 연속일때 최대
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
d = [[0]*3 for _ in range(n)]
d[0][1] = a[0]
for i in range(1, n):
    d[i][0] = max(d[i-1])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]
print(max(d[n-1]))