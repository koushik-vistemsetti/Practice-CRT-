# angram
'''
s1 = input()
s2 = input()
d = {}
d1 = {}
if(len(s1) == len(s2)):
    for i in s1:    
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d1: 
            d1[i] += 1
        else:
            d1[i] = 1
    print("Anagram" if d == d1 else "Not Anagram")
else:
    print("Not Anagram")
'''
# PANAGRAM
'''
s = input().lower()
d = {}
if (len(s) >= 26):
    for ele in s:
        if ele in 'qwertyuiopasdfghjklzxcvbnm':
            d[ele] = 1
print("Panagram" if (len(d) == 26) else "Not Panagram")
'''
n = input()
a = input()
c = 0
w = len(a)
d, d1 = {}, {}
l = 0
for x in a:
    if (x in d1):
        d1[x] += 1
    else:
        d1[x] = 1
for r in range(len(n)):
    if (n[r] in d):
        d[n[r]] += 1
    else:
        d[n[r]] = 1
    if (r >= w-1):
        if (d == d1):
            c += 1
        d[n[l]] -= 1
        if (d[n[l]] == 0):
            d.pop(n[l])
        l += 1
print(c)
# ANAGRAM IN EVERY WINDOW OR NOT
'''
s=input("Enter main text")
s1=input("Test string:")
d={}
l=0
c=0
for r in range(len(s)):
'''
# longest sequence of 1's where k is replacement
