MOD = 1000000000
def f(cnt, cur):
    if cnt == n:
        return 1
    if cur == 0:
        return f(cnt+1, 1)
    elif cur == 9:
        return f(cnt+1, 8)
    else:
        return f(cnt+1, cur-1) + f(cnt+1, cur+1)
n = int(input())
ans = 0
for i in range(1, 10):
    ans += f(1, i)
print(ans%MOD)