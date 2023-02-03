# 	61916KB	6220ms

# 3가지 방법으로 구현: adjacency-array, adjacency-list, edge list
n, m = map(int, input().split())
edges = [] # edge list
a = [[False]*n for _ in range(n)] # adjacency-array
g = [[] for _ in range(n)] # adjacency-list
for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x,y))
    edges.append((y,x))
    a[x][y] = a[y][x] = True
    g[x].append(y)
    g[y].append(x)
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            exit()
print(0)