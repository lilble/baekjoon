# 	31256KB	220ms

# Bottom-Up

n = int(input())
p = list(map(int,input().split()))
d = [0]*(n+1)
for x in range(1, n+1):
    d[x] = p[x-1]
    for i in range(1,x):
        d[x] = max(d[x], p[x-1-i]+d[i])
print(d[n])