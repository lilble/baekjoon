# 48140KB	156ms

from collections import deque
MAX = 100000
n, k = map(int, input().split())
bef = [-1]*(MAX+1)
time = [-1]*(MAX+1)
q = deque()
q.append(n)
time[n] = 0
def find():
    while q:
        cur = q.popleft()
        if cur == k:
            return
        for x in [cur+1, cur-1, cur*2]:
            if 0<=x<=MAX and time[x] == -1:
                time[x] = time[cur]+1
                q.append(x)
                bef[x] = cur
find()
print(time[k])
ans = deque()
idx = k
while idx != -1:
    ans.appendleft(idx)
    idx = bef[idx]
print(' '.join(map(str, ans)))