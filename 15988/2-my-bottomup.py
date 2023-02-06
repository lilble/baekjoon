# pypy3:	122144KB	668ms

import sys
input = sys.stdin.readline
MOD = 1000000009
MAX = 1000000
d = [0]*(MAX+1) 
d[0] = 1
d[1] = 1
d[2] = 2
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2] + d[i-3])%MOD
    print(d[n])