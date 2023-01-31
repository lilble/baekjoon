# d[i] = a[i]를 마지막으로 하는 가장 긴 증가하는 부분수열 길이
# v[i] = a[i]의 앞에 와야 하는 수의 인덱스
n = int(input())
a = list(map(int, input().split()))
d = [1]*n
v = [-1]*n
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j] and d[i]<d[j]+1:
            d[i] = d[j]+1
            v[i] = j
num = max(d)
idx = d.index(num)
ans = []
while idx >= 0:
    ans.insert(0, a[idx])
    idx = v[idx]
print(num)
print(' '.join(map(str,ans)))