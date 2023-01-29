# 	30616KB	3584ms
# 순열 이용

n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, 1<<n):
    add = 0
    for k in range(n):
        if i&(1<<k):
            add += a[k]
    if add == s:
        ans += 1
print(ans)