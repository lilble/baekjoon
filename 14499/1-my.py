# 	31256KB	44ms

n, m, x, y, k = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
d = [0]*6
for c in commands:
    if c==1:
        if y >= m-1:
            continue
        y += 1
        d = [d[1], d[5], d[2], d[3], d[0], d[4]]
    elif c==2:
        if y <= 0:
            continue
        y -= 1
        d = [d[4], d[0], d[2], d[3], d[5], d[1]]
    elif c==3:
        if x <= 0:
            continue
        x -= 1
        d = [d[3], d[1], d[0], d[5], d[4], d[2]]
    elif c==4:
        if x >= n-1:
            continue
        x += 1
        d = [d[2], d[1], d[5], d[0], d[4], d[3]]
    print(d[-1])
    if a[x][y] == 0:
        a[x][y] = d[0]
    else:
        d[0] = a[x][y]
        a[x][y] = 0