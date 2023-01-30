# 30616KB	48ms

def go(cnt, s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(cnt+1, s+i, goal)
    return now
t = int(input())
for _ in range(t):
    n = int(input())
    print(go(0, 0, n))