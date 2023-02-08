# 31256KB	276ms

n = int(input())
a = list(map(int, input().split()))
front = [1]*n # 앞부분부터 증가
back = [1]*n # 뒷부분부터 증가
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            front[i] = max(front[i], front[j]+1)
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if a[i] > a[j]:
            back[i] = max(back[i], back[j]+1)
tot = []
for i in range(n):
    tot.append(front[i]+back[i])
print(max(tot)-1)