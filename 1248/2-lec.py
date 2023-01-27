n = int(input())
ans = [11]*n
s = input()
sign = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i, n):
        char = s[cnt]
        if char == '+':
            sign[i][j] = 1
        elif char == '-':
            sign[i][j] = -1
        cnt += 1
def check(idx):
    tot = 0
    for i in range(idx, -1, -1):
        tot += ans[i]
        if tot*sign[i][idx] > 0:
            continue
        elif tot == 0 and sign[i][idx] == 0:
            continue
        else:
            return False
    return True
def f(idx):
    if idx == n:
        return True
    if sign[idx][idx] == 0:
        ans[idx] = 0
        if check(idx) and f(idx+1):
            return True
    for i in range(1, 11):
        ans[idx] = sign[idx][idx]*i
        if check(idx) and f(idx+1):
            return True
    return False
if f(0):
    print(' '.join(map(str, ans)))