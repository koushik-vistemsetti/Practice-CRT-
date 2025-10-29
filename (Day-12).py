
# open close

m = []
'''

def brac(o, c, s):

    if (o == 0 and c == 0):
        m.append(s)
        return
    if (o == c):
        s = s+'('
        o -= 1
    if (o == 0):
        while (c):
            s = s+')'
            c -= 1
        m.append(s)
        return
    brac(o-1, c, s+'(')
    brac(o, c-1, s+')')
    return m


print(*brac(3, 3, ''))
'''

'''
def brac(o, c, s):

    if (o == 0 and c == 0):
        m.append(s)
        return
    if (o > 0):
        brac(o-1, c, s+'(')
    if (c > o):
        brac(o, c-1, s+')')
    return m


print(*brac(3, 3, ''))

'''
'''

def f(n, z, s):
    if (n == 0):
        m.append(s)
        return
    if (z > n//2):
        while n:
            s = s+'1'
            n -= 1
        f(n, z, s)
        return
    f(n-1, z, s+'1')
    f(n-1, z+1, s+'0')
    return m


print(f(3, 0, ''))

'''
# quick  using recursions


def qs(li, l, r):
    if l >= r:
        return
    p = l
    i = l+1
    j = r
    while i <= j:
        if li[i] < li[p]:
            i += 1
        elif li[j] > li[p]:
            j -= 1
        else:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
    li[p], li[j] = li[j], li[p]
    qs(li, l, j-1)
    qs(li, j+1, r)
    return li


li = [42, 17, 93, 8, 61, 29, 55]
print(qs(li, 0, len(li)-1))
