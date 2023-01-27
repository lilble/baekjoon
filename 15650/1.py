# 	30616KB	36ms
# 방법 1. 각 위치에 무슨 수를 넣을지
a = []
def func(n, m, idx):
    if len(a) == m:
        print(' '.join(map(str, a)))
        return
    for i in range(idx, n+1):
        a.append(i)
        func(n, m, i+1)
        a.pop()
n, m = map(int, input().split())
func(n, m, 1)