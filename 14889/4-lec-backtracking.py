# 30616KB	2656ms

def f(idx, a, b):
    if idx == n:
        if len(a) != n//2: # here is backtracking
            return -1
        if len(b) != n//2: # here is backtracking
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[a[i]][a[j]]
                t2 += s[b[i]][b[j]]
        diff = abs(t1-t2)
        return diff
    if len(a) > n//2 or len(b) > n//2:
        return -1
    ans = -1
    t1 = f(idx+1, a+[idx], b)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = f(idx+1, a, b+[idx])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(f(0, [], []))