# Recursion error - recursion 한도 초과인듯.

def f(idx):
    if idx == n:
        return 1
    if idx > n:
        return 0
    return f(idx+1) + f(idx+2)
n = int(input())
print(f(0)%10007)