# 30616KB	148ms
n = int(input())
able = [True]*(n+1)
def f(cnt, a):
    if cnt == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, n+1):
        if able[i]:
            able[i] = False
            f(cnt+1, a+[i])
            able[i] = True    
f(0, [])