# 	32308KB	4024ms

# d(n, k) = k개 정수 합이 n이 되는 경우의 수
# d(0, x) = 1
MOD = 1000000000
def f(cn, ck):
    if cn != 0 and ck == 0:
        return 0
    if d[cn][ck] > 0:
        return d[cn][ck]
    for i in range(cn+1):
        d[cn][ck] += f(i, ck-1)
    d[cn][ck] %= MOD
    return d[cn][ck]
n, k = map(int, input().split())
d = [[0]*(k+1) for _ in range(n+1)]
d[0] = [1]*(k+1)
print(f(n, k))