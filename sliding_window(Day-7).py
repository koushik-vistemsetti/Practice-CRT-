# sliding window sum of x numbers
'''
l = list(map(int, input().split()))
x = int(input())
for i in range(len(l)-(x-1)):
    n = 0
    for j in range(i, i+x):
        n += l[j]
    print(n, end=' ')
'''
# 0r
'''
i,j,s=0
while j<len(l):
    s+=l[j]
    if(j-i+1<x):
        j+=1
    elif(j-i+1==x):
        print(s,end=" ")
        s-=l[i]
        i+=1
        j+=1
'''
# 2.sliding window with checking minimum and maximum sum and also print the contribution of that
'''
l = list(map(int, input().split()))
x = int(input())
i, j, s = 0, 0, 0
mi = 0
ma = 0
while j < len(l):
    s += l[j]
    if (j-i+1 < x):
        j += 1
    elif (j-i+1 == x):
        mi = s if (mi < s) else mi
        ma = s if (ma > s) else ma
        print(s, end=" ")
        s -= l[i]
        i += 1
        j += 1
print()
print(mi, ma)
'''
# 3.s="abacddcbkbb" if the sliding window contains all unique character print those (dont use slicing)
'''
s, x = input().lower(), int(input())
i, ch = 0, ""
for j in range(len(s)):
    ch += s[j]
    if j-i+1 == x:
        if len(set(ch)) == x:
            print(ch, end=" ")
        i, ch = i+1, ch[1:]
    j += 1
'''
# 4.s="abacddcbkbb" if the sliding window contains all unique character print those (dont use slicing)using dictionary

s = 'abacddcbkbb'
x = int(input())
i = 0
d = {}
for j in range(len(s)):
    if s[j] in d:
        d[s[j]] += 1
    else:
        d[s[j]] = 1
    if j-i+1 == x:
        if len(d) == x:
            print(*d)
        d[s[i]] -= 1
        if d[s[i]] == 0:
            d.pop(s[i])
        i += 1
