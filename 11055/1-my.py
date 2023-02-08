# 	31256KB	164ms

# d[i] = i사용, 1~i 번째까지 최대
n = int(input())
a = list(map(int, input().split()))
d = list(a)
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + a[i])
print(max(d))