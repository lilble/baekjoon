# python은 top-down으로 풀 수 없다.
# 재귀를 쓰면 시간초과, 메모리 너무 많이 차지.
# python은 다이나믹을 풀 때 Bottom-up을 쓰는 게 좋다!
# Top-down
def f(n):
    if n == 1:
        return 0
    if note[n] > 0:
        return note[n]
    note[n] = f(n-1)+1
    if n%3 == 0:
        note[n] = min(note[n], f(n//3)+1) 
    if n%2 == 0:
        note[n] = min(note[n], f(n//2)+1)
    return note[n]
x = int(input())
note = [0]*(x+1)
print(f(x))