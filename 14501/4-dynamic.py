# 	31388KB	60ms

# dynamic. O()

# d[i] = 1일~(i+1)일까지 일할 때 최대수익
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [0]*(n+1)
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
for i in range(1, n+1):
    for j in range(i):
        if t[j+1] <= i-j:
            d[i] = max(d[i], d[j]+p[j+1])
print(d[n])