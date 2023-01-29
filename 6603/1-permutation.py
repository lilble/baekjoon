# 30616KB	36ms

# 순열
def nextp(s):
    i = j = k = len(s)-1
    while s[i-1]>=s[i]:
        i-=1
        if i<=0:
            return False
    while s[i-1]>=s[j]:
        j-=1
    s[i-1],s[j] = s[j],s[i-1]
    while i<k:
        s[i],s[k] = s[k],s[i]
        i+=1
        k-=1
    return True
def get(a, s, ans):
    for i in range(len(s)):
        if s[i] == 1:
            ans.append(a[i])
while True:
    a = list(map(int,input().split()))
    k = a[0]
    if k == 0:
        break
    s = [1]*6 + [2]*(k-6)
    while True:
        ans = []
        get(a[1:], s, ans)
        print(' '.join(map(str,ans)))
        if not nextp(s):
            break
    print()