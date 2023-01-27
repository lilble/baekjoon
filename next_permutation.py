a = [] # given permutation
def next_permutation(a, n):
    i = n-1 
    while a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = n-1
    while a[i-1] >= a[j]:
        j -= 1
    swap(a[i-1], a[j])
    k = n-1
    while i < k:
        swap(a[i], a[k])
        i += 1
        k -= 1
    return True