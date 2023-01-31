#38964KB	96ms

n = int(input())
a = list(map(int, input().split()))
d = list(a)
for i in range(1, n):
    d[i] = max(a[i], d[i-1]+a[i])
print(max(d))