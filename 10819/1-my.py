#	116968KB	180ms
# pypy3

def calc(l):
    s = 0
    for i in range(0, n-1):
        s += abs(l[i] - l[i+1])
    return s
def f(cnt, b):
    global m
    if cnt == n:
        m = max(m, calc(b))
        return
    for i in range(n):
        if able[i]:
            able[i] = False
            f(cnt+1, b+[a[i]])
            able[i] = True
n = int(input())
a = list(map(int, input().split()))
able = [True]*n
m = 0
f(0, [])
print(m)