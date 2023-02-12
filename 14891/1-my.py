# 	31256KB	44ms

# f(gn, rot, direction)
# gn = gear number, rot = gn이 rotation할 방향
# direction = 진행방향 (right = 1, left = -1)
gears = [list(map(int, input())) for _ in range(4)]

def rotate(gn, rot):
    cur = gears[gn]
    if rot == 1:
        gears[gn] = [cur[-1]] + cur[:-1]
    else:
        gears[gn] = cur[1:] + [cur[0]]
        
def f(n, rot, direction):
    cur = gears[n]
    if direction == 1:
        if gears[n-1][2] != cur[6]:
            if n < 3:
                f(n+1, (-1)*rot, 1)
            rotate(n, rot)
    else: 
        if gears[n+1][6] != cur[2]:   
            if n > 0:
                f(n-1, (-1)*rot, -1)
            rotate(n, rot)
            
k = int(input())
for _ in range(k):
    n, rot = map(int, input().split())
    n -= 1
    if n > 0:
        f(n-1, (-1)*rot, -1)
    if n < 3:
        f(n+1, (-1)*rot, 1)
    rotate(n, rot)
ans = 0
mul = [1,2,4,8]
for i in range(4):
    ans += mul[i]*gears[i][0]
print(ans)