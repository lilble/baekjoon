#	38232KB	544ms

# Bottom-up
x = int(input())
note = [0]*(x+1)
for i in range(2, x+1):
    note[i] = note[i-1]+1
    if i%3 == 0:
        note[i] = min(note[i], note[i//3]+1)
    if i%2 == 0:
        note[i] = min(note[i], note[i//2]+1)
print(note[x])