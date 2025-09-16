# 1.frequency of each number
'''
n = list(map(int, input().split()))
f = {}
for i in n:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print(f)
'''
# 2.highest frequency number should be printed
'''
n = list(map(int, input().split()))
f = {}
for i in n:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print(max(f, key=f.get))
'''
# find missing number
'''
n = list(map(int, input().split()))
s = set(n)
mi = min(s)5 6 5 3 4 8 5 6
ma = max(s)
for i in range(mi, ma+1):
    if i not in s:
        print(i)
        break
'''
# 4.n=5 6 5 3 4 8 5 6 output 3= [3, 2, 3, 1, 1, 1, 3, 2]
'''
n = list(map(int, input().split()))
d = []
for e in n:
    c = 0
    for f in n:
        if e == f:
            c += 1
    d.append(c)
print(d)
'''  # 4.n=5 6 5 3 4 8 5 6 output 3= [3, 2, 3, 1, 1, 1, 3, 2]
# 4.n=5 6 5 3 4 8 5 6 output 3= [3, 2, 3, 1, 1, 1, 3, 2]
# n = list(map(int, input().split()))

# 5.rotate a list(right to left)
'''
n = list(map(int, input().split()))
x = int(input())
for i in range(x):
    n.insert(0, n.pop())
print(n)
'''
# 5.rotate a list(left to right)
'''
n = list(map(int, input().split()))
x = int(input())
for i in range(x):
    n.append(n.pop(0))
print(n)
'''
# 6.rotate a list in specific area
'''
n = list(map(int, input().split()))
x, y = map(int, input().split())
t = input()
if t == 'l':
    y1 = n.pop(y)
    n.insert(x, y1)
elif t == 'r':
    y1 = n.pop(x)
    n.insert(y, y1)
print(n)
'''
# 7.selection sort
'''
n = list(map(int, input().split()))
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
print(n)
'''
# 8.bubble sort
'''
l=list(map(int,input().split()))
while(1):
    c=0
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
            c=1
    if(c==0):
        break    
print(l)
'''
# 9.insertion sort

l = list(map(int, input().split()))
for i in range(1, len(l)):
    j = i
    while (j > 0 and l[j] < l[j-1]):
        l[j], l[j-1] = l[j-1], l[j]
        j -= 1
print(l)
