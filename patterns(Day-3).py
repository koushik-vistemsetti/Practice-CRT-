'''
n=int(input())
for i in range(1,n*2):
    for j in range(1,n+1+1):
        p=j
        if p<=i:
            print("@",end=' ')
        else:
            print("* ",end='')
    print()
    if i==n:
        p-=1
    elif i>=n:
        p+=1
'''
#
'''
n=int(input())
for i in range(1,n*2):
    for j in range(1,n+1+1):
        if j<=i:
            print("@",end=' ')
        else:
            print("* ",end='')
    print()
    if i==n:
        p-=1
    elif i>=n:
        p+=1
'''
#3
'''
n=int(input())
p=n
q=n+2
for i in range(1,n*2):
    for j in range(1,n*2+1+1):
        if j<=p or j>=q :
            print("*",end=' ')
        else:
            print("@",end='')
    print()
    if i<n :
        p-=1
        q+=1
    else:
        p+=1
        q-=1
'''
#4
'''
n=int(input())
p=n+1
q=n+1
for i in range(0,n*2+1):
    for j in range(1,n*2+1+1):
        if j<=p or j>=q :
            print("*",end=' ')
        else:
            print("@",end='')
    print()
    if i<n :
        p-=1
        q+=1
    else:
        p+=1
        q-=1
'''
#5.
'''
n=int(input())
p=n
q=n+2
for i in range(1,n*2):
    for j in range(1,n*2+1  ):
        if j<=p or j>=q :
            print(" ",end=' ')
        else:
            print("*",end='')
    print()
    if i<n :
        p-=1
        q+=1
    else:
        p+=1
        q-=1
'''
#6.
'''
n=int(input())
p=1
for i in range(1,n*2):
    for j in range(1,n*2+1):
        if(i%2==0):
            if(j!=1):
                print(i,end=' ')
            else:
                print(i+1,end=' ')
        else:
            if(j!=n*2):
                print(i,end=' ')
            else:
                print(i+1,end=' ')
    print()
'''
#8.
'''
n=int(input())
for i in range(n*2-1):
    for j in range(i,n*2-1):
        if(j%2==0):
            print(1,end=' ')
        else:
            print(0 ,end=' ')
    print()
'''
#2.
'''
n=int(input())
p=n
for i in range(n*2+2):
    for j in range(1,n+2):
        if(j<=p):
            print(" ",end=' ')
        else:
            print(" *",end=' ')
    print()
    if(i<n):
        p-=1
    else:
        p+=1
'''







        
