# adjacency-array
# O(V^2)
# dfs(1) ~ dfs(V) 까지 호출할 것임. 모든 정점에 대해 호출
def dfs(x):
    check[x] = True
    for i in range(1, n+1):
        if a[x][i] == 1 and check[i] == False:
            dfs(i)

# adjacency-list
# O(V+E) ~= O(E)
# dfs(1) ~ dfs(V) 까지 호출할 것임. 모든 정점에 대해 호출
def dfs(x):
    check[x] = True
    for i in a[x]:
        if check[i] == False:
            dfs(i)

# edge list
def dfs(x):
    check[x] = True
    