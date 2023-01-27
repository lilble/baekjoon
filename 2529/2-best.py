#31576KB	172ms

def ok(idx, i, ans):
    if idx == 0:
        return True
    if able[i] == False:
        return False
    prev = int(ans[idx-1])
    ineq = s[idx-1]
    if (ineq == '<' and prev < i) or (ineq == '>' and prev > i):
        return True
def f(idx, ans):
    if idx == n+1:
        answers.append(ans)
        return 
    for i in range(10):
        if ok(idx, i, ans):
            able[i] = False
            f(idx+1, ans+str(i))
            able[i] = True
n = int(input())
s = list(map(str, input().split()))
able = [True]*10
answers = []
f(0, '')
print(answers[-1])
print(answers[0])