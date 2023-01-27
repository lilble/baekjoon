# 30748KB	160ms
a = []
used = [False]*9
def func(n, m, cnt):
    if m == cnt:
        print(' '.join(map(str, a)))
    for i in range(1, n+1):
        if used[i]:
            continue
        used[i] = True
        a.append(i)
        func(n, m, cnt+1)
        a.pop()
        used[i] = False
n, m = map(int, input().split())
func(n, m, 0)