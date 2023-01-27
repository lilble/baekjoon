# 30616KB	144ms

n = int(input())
s = list(map(str, input().split()))
able = [True]*10
mini = 9999999999
maxi = 0
zero = False
def f(idx, prev, ans):
    global mini, maxi, zero
    if idx == n:
        if ans[0] == 0:
            zero = True
        ansi = int(''.join(map(str, ans)))
        mini = min(mini, ansi)
        maxi = max(maxi, ansi)
        return 
    for i in range(10):
        ok = False
        if prev == -1:
            ok = True
        elif able[i]:
            if (s[idx] == '<' and prev < i) or (s[idx] == '>' and prev > i):
                ok = True
        if ok:
            able[i] = False
            f(idx+1, i, ans+[i])
            able[i] = True
f(-1, -1, [])
print(maxi)
if zero:
    print('0'+str(mini))
else:
    print(mini)