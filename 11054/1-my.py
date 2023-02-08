# 31256KB	284ms

# d[i][0] = i포함, 0~i 까지 중 증가 최대길이
# d[i][1] = i포함, 감소
n = int(input())
a = list(map(int, input().split()))
d = [[1]*2 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i][0] = max(d[i][0], d[j][0] + 1)
        elif a[j] > a[i]:
            d[i][1] = max(d[i][1], max(d[j]) + 1)
ans = 0
for i in range(n):
    for j in range(2):
        ans = max(ans, d[i][j])
print(ans)