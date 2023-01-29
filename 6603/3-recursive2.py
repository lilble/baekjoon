# 30616KB	40ms

def f(cnt, k, s, ans, idx):
    if cnt == 6:
        print(' '.join(map(str,ans)))
        return
    if idx >= k:
        return
    f(cnt+1, k, s, ans+[s[idx]], idx+1)
    f(cnt, k, s, ans, idx+1)
while True:
    a = list(map(int, input().split()))
    k = a[0]
    if k == 0:
        break
    s = a[1:]
    f(0, k, s, [], 0)
    print()