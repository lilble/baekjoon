#30616KB	180ms
# 무식한 방법. 인강에 나옴
def get(n):
    ans = 0
    for l1 in range(1, 4):
        if l1 == n:
            ans += 1
        for l2 in range(1, 4):
            if l1 + l2 == n:
                ans += 1
            for l3 in range(1, 4):
                if l1 + l2 + l3 == n:
                    ans += 1
                for l4 in range(1, 4):
                    if l1 + l2 + l3 + l4 == n:
                        ans += 1
                    for l5 in range(1, 4):
                        if l1 + l2 + l3 + l4 + l5 == n:
                            ans += 1
                        for l6 in range(1, 4):
                            if l1 + l2 + l3 + l4 + l5 + l6 == n:
                                ans += 1
                            for l7 in range(1, 4):
                                if l1 + l2 + l3 + l4 + l5 + l6 + l7 == n:
                                    ans += 1
                                for l8 in range(1, 4):
                                    if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == n:
                                        ans += 1
                                    for l9 in range(1, 4):
                                        if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 == n:
                                            ans += 1
                                        for l10 in range(1, 4):
                                            if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 == n:
                                                ans += 1
    return ans
                            
num = int(input())
for _ in range(num):
    n = int(input())
    print(get(n))