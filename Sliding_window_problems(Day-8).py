# 1.find the maximum element in every window
'''
li = list(map(int, input().split()))
n = int(input())
ma = 0
for i in range(len(li)-n+1):
    ma = li[i]
    for j in range(i+1, i+n):
        if (li[j] > ma):
            ma = li[j]
    print(ma, end=" ")
'''
# 0r
'''
l=list(map(int,input().split()))
n=int(input())
t=[]
i,j=0,0
while j<len(l):
    t.append(l[j])
    if len(t)==n:
        m=t[0]
        for x in t:
            if x>m:
                m=x
        print(m,end=" ")
        t.pop(0)
        i+=1
    j+=1
'''
# 2.find the first minimum value in every window
'''
l=list(map(int,input().split()))
n=int(input())
t=[]
i,j=0,0
while j<len(l):
    t.append(l[j])
    if len(t)==n:
        m=t[0]
        for x in t:
            if x<m:
                m=x
        print(m,end=" ")
        t.pop(0)
        i+=1
    j+=1
'''
# 3.first negative value in every window
l = list(map(int, input().split()))
k = int(input())
i = j = 0
t = []
while (j < len(l)):
    if (l[j] < 0):
        t.append(l[j])
    if (j-i+1 < k):
        j += 1
    elif (j-i+1 == k):
        if (len(t) != 0):
            print(t[0], end=" ")
            if (t[0] == l[i]):
                t.remove(t[0])
        else:
            print(0, end=" ")
        i += 1
        j += 1
