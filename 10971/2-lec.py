# 	115244KB	540ms
# pypy3

def nextp(a):
    i = j = k = n-1
    while a[i-1] >= a[i]:
        i -= 1
        if i <= 0:
            return False
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1],a[j] = a[j],a[i-1]
    while i<k:
        a[i],a[k] = a[k],a[i]
        i += 1
        k -= 1
    return True
n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
city = list(range(n))
ans = 2147483647
while True:
    ok = True
    s = 0
    for i in range(0, n-1):
        if w[city[i]][city[i+1]] == 0:
            ok = False
            break
        else:
            s += w[city[i]][city[i+1]]
    if ok and w[city[-1]][city[0]] != 0:
        s += w[city[-1]][city[0]]
        ans = min(ans, s)
    if not nextp(city):
        break
print(ans)