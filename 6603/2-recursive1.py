# 30616KB	40ms

# 재귀
def f(cnt, k, s, ans, idx):
    if cnt == 6:
        print(' '.join(map(str,ans)))
        return
    for i in range(idx, k):
        f(cnt+1, k, s, ans+[s[i]], i+1)
while True:
    a = list(map(int, input().split()))
    k = a[0]
    if k == 0:
        break
    s = a[1:]
    f(0, k, s, [], 0)
    print()