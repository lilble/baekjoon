# 31256KB	1660ms

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
for c in commands:
    if c==3 or c==4:
        tmp = [[0]*n for _ in range(m)]
        if c==3:
            for i in range(n):
                for j in range(m):
                    tmp[j][-1-i] = a[i][j]
        elif c==4:
            for i in range(n):
                for j in range(m):
                    tmp[-1-j][i] = a[i][j]
        a = tmp
        n, m = m, n
    else:
        tmp = [[0]*m for _ in range(n)]
        if c==1:
            for i in range(n):
                tmp[n-1-i] = a[i]
        if c==2:
            for i in range(n):
                for j in range(m):
                    tmp[i][j] = a[i][m-1-j]
        if c==5:
            for i in range(n//2):
                for j in range(m//2):
                    tmp[i][j+m//2] = a[i][j]
                for j in range(m//2, m):
                    tmp[i+n//2][j] = a[i][j]
            for i in range(n//2, n):
                for j in range(m//2):
                    tmp[i-n//2][j] = a[i][j]
                for j in range(m//2, m):
                    tmp[i][j-m//2] = a[i][j]
        if c==6:
            for i in range(n//2):
                for j in range(m//2):
                    tmp[i+n//2][j] = a[i][j]
                for j in range(m//2, m):
                    tmp[i][j-m//2] = a[i][j]
            for i in range(n//2, n):
                for j in range(m//2):
                    tmp[i][j+m//2] = a[i][j]
                for j in range(m//2, m):
                    tmp[i-n//2][j] = a[i][j]
        a = tmp
for r in a:
    print(' '.join(map(str, r)))