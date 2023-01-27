# 	30616KB	48ms

l, c = map(int, input().split())
a = list(map(str, input().split()))
a.sort()
def f(cnt, idx, s):
    if cnt > l:
        return
    if cnt == l:
        v = 0
        for x in s:
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                v += 1
        if v >= 1 and v <= l-2:
            print(s)
        return
    for i in range(idx, c):
        f(cnt+1, i+1, s+a[i])
f(0, 0, '')