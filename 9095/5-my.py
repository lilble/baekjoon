#	30616KB	36ms

def f(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    cur = 0
    for i in range(1, 4):
        cur += f(n-i)
    return cur
t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))