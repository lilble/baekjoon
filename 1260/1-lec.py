# 32372KB	444ms

n, m, v = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
for row in a:
    row.sort()
    
def dfs(node):
    global able
    able[node] = False
    print(node, end=' ')
    for i in a[node]:
        if able[i]:
            dfs(i)

def bfs():
    q = [v]
    able[v] = False
    while q:
        node = q.pop(0)
        print(node, end=' ')
        for i in a[node]:
            if able[i]:
                able[i] = False
                q.append(i)
able = [True]*(n+1)
dfs(v)
print()
able = [True]*(n+1)
bfs()
print()