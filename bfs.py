# adjacency-array
# O(V^2)
q = []
check[1] = True
q.append(1)
while q:
    x = q.pop(0)
    for i in range(1, n+1):
        if a[x][i] == 1 and check[i] == False:
            check[i] = True
            q.append(i)

# adjacency-list
# O(V+E) ~= O(E)
q = []
check[1] = True
q.append(1)
while q:
    x = q.pop(0)
    for i in a[x]:
        if check[i] == False:
            check[i] = True
            q.append(i)

# Edge list 
