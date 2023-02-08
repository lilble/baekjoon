# 	31256KB	44ms

# d[i] = 3xi 경우의 수 = (d[0]+...+d[i-4])*2 + d[i-2]*3
n = int(input())
d = [0]*31
d[0] = 1
for i in range(2, 31, 2):
    d[i] = sum(d[0:i-1])*2 + d[i-2]
print(d[n])