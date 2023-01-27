#30616KB	72ms
def find(n):
    ans = 0
    if n == 0:
        return 1
    for i in range(1,4):
        if n >= i:
            ans = ans + find(n-i)
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    print(find(n))