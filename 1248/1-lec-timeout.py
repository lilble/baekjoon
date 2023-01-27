n = int(input())
s = input()
sign = [[2]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
ans = [11]*n
def ok():
    for i in range(n):
        tot = 0
        for j in range(n):
            tot += ans[j]
            if sign[i][j]*tot > 0:
                continue
            if sign[i][j] == 0 and tot == 0:
                continue
            return False
    return True
def f(idx):
    if idx == n:
        return ok()
    if sign[idx][idx] == 0:
        ans[idx] = 0
        return f(idx+1)
    for i in range(1, 11):
        ans[idx] = i*sign[idx][idx] # ans[idx]의 부호 == sign[idx][idx]
        if f(idx+1):
            return True
    return False
if f(0):
    print(ans)