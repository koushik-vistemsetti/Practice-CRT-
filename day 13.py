# merge sort using recursions
def ms(l):
    if len(l) == 1:
        return l
    m = len(l)//2
    left = ms(l[:m])
    right = ms(l[m:])
    return merge(left, right)


def merge(left, right):
    nl = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nl.append(left[i])
            i += 1
        else:
            nl.append(right[j])
            j += 1
    while i < len(left):
        nl.append(left[i])
        i += 1
    while j < len(right):
        nl.append(right[j])
        j += 1
    return nl


print(ms([9, 8, 7, 6, 5, 4, 3, 2, 1]))
