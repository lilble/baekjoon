# 	70812KB	424ms

MOD = 1000000009
MAX = 1000000
d = [0]*(MAX+1)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, MAX+1):
    d[i] = (d[i-1] + d[i-2] + d[i-3])%MOD
t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])