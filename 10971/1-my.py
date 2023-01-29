# 	30616KB	5872ms
# pypy3 : 	115340KB	664ms

def calc(a):
    s = 0
    for i in range(len(a)-1):
        cost = w[a[i]][a[i+1]]
        if cost == 0:
            return -1
        s += cost
    cost = w[a[-1]][a[0]]
    if cost == 0:
        return -1
    s += cost
    return s
def f(a):
    i = j = k = n-1
    while a[i-1] >= a[i]:
        i-=1
        if i<=0:
            return False
    while a[i-1] >= a[j]:
        j-=1
    a[i-1], a[j] = a[j], a[i-1]
    while i<k:
        a[i], a[k] = a[k], a[i]
        i+=1
        k-=1
    return True
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
a = list(range(n))
m = 2147483647
while True:
    c = calc(a)
    if c != -1:
        m = min(m, c)
    if not f(a):
        break
print(m)