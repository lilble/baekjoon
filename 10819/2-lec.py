#	30616KB	104ms

def calc(a):
    s = 0
    for i in range(len(a)-1):
        s += abs(a[i]-a[i+1])
    return s
def nextp(a):
    i = j = k = len(a)-1
    while a[i-1] >= a[i]:
        i-=1
        if i <= 0:
            return False
    while a[i-1] >= a[j]:
        j-=1
    a[i-1], a[j] = a[j], a[i-1]
    while i < k:
        a[i], a[k] = a[k], a[i]
        i+=1
        k-=1
    return True
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = 0
while True:
    m = max(m, calc(a))
    if not nextp(a):
        break
print(m)