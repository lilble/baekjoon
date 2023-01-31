# 31256KB	120ms

n = int(input())
a = list(map(int, input().split()))
d = []
for i in range(n):
    d.append([1, [a[i]]])
for i in range(1,n):
    for j in range(i):
        if a[i] > a[j] and d[i][0] < d[j][0]+1:
            d[i][0] = d[j][0]+1
            d[i][1] = d[j][1]+[a[i]]
idx = 0
maximum = d[0][0]
for i in range(1, n):
    if maximum < d[i][0]:
        idx = i
        maximum = d[i][0]
print(d[idx][0])
print(' '.join(map(str, d[idx][1])))