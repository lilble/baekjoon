def f(a, n):
    i = j = k = n-1
    while a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    while i < k:
        a[i], a[k] = a[k], a[i]
        i += 1
        k -= 1
    return True
n = int(input())
a = list(map(int, input().split()))
if f(a, n):
    print(' '.join(map(str, a)))
else: 
    print(-1)