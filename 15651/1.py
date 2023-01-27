a = []
def func(n, m, cnt):
    if cnt == m:
        print(' '.join(map(str, a)))
        return
    for i in range(1, n+1):
        a.append(i)
        func(n, m, cnt+1)
        a.pop()
n, m = map(int, input().split())
func(n, m, 0)