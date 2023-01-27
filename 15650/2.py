# 	30616KB	36ms
# 방법 2. 숫자를 넣을지 말지
a = []
def func(n, m, idx, cnt):
    if cnt == m:
        print(' '.join(map(str, a)))
        return
    if idx > n:
        return
    a.append(idx)
    func(n, m, idx+1, cnt+1)
    a.pop()
    func(n, m, idx+1, cnt)
n, m = map(int, input().split())
func(n, m, 1, 0)