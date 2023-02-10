# 	31256KB	460ms

n, m, r = map(int, input().split())
nh = n//2
mh = m//2
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
for c in commands:
    if c == 1:
        a = a[::-1]
    elif c == 2:
        for i in range(mh):
            for r in a:
                r[i], r[-1-i] = r[-1-i], r[i]
    elif c == 3:
        new = []
        for j in range(mh*2):
            new.append([i[j] for i in a][::-1])
        a = new
        nh, mh = mh, nh
    elif c == 4:
        new = []
        for j in range(mh*2-1, -1, -1):
            new.append([i[j] for i in a])
        a = new
        nh, mh = mh, nh
    elif c == 5:
        new = []
        for i in range(nh):
            new.append(a[i+nh][:mh] + a[i][:mh])
        for i in range(nh):
            new.append(a[i+nh][mh:] + a[i][mh:])
        a = new
    elif c == 6:
        new = []
        for i in range(nh):
            new.append(a[i][mh:] + a[i+nh][mh:])
        for i in range(nh):
            new.append(a[i][:mh] + a[i+nh][:mh])
        a = new
for x in a:
    print(' '.join(map(str, x)))