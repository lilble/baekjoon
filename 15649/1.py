# 	30616KB	148ms
a = [0]*8
used = [False]*9
def func(n, m, cnt):
    if m == cnt:
        print(' '.join(map(str, a[0:m])))
    for i in range(1, n+1):
        if used[i]:
            continue
        used[i] = True
        a[cnt] = i
        func(n, m, cnt+1)
        used[i] = False
n, m = map(int, input().split())
func(n, m, 0)