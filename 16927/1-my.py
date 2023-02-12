# 	34992KB	124ms

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
groups = []
groupn = min(n, m)//2
for k in range(groupn):
    group = a[k][k:m-k] + [i[m-1-k] for i in a[k+1:n-1-k]] + a[n-1-k][m-1-k:k:-1] + [i[k] for i in a[n-1-k:k:-1]]
    groups.append(group)
for k in range(groupn):
    group = groups[k]
    l = len(group)
    idx = r%l
    for j in range(k, m-k):
        a[k][j] = group[idx]
        idx = (idx+1)%l
    for i in range(k+1, n-1-k):
        a[i][m-1-k] = group[idx]
        idx = (idx+1)%l
    for j in range(m-1-k, k, -1):
        a[n-1-k][j] = group[idx]
        idx = (idx+1)%l
    for i in range(n-1-k, k, -1):
        a[i][k] = group[idx]
        idx = (idx+1)%l
for row in a:
    print(' '.join(map(str, row)))df