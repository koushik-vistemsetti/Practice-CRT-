import math as m
#1.factors of given number
'''
n=int(input())
c=0
for i in range(1,m.isqrt(n)+1):
    if(n%i==0):
        if(n//i==i):
            print(i)
        else:
            print(i,n//i)
    if(n//i==i):
        c+=1
    else:
        c+=2
if(c%2!=0):
    print('perfect square')
else:
    print('not perfect square')
'''
#2.check prime
'''
n=int(input())
c=0
for i in range(1,m.isqrt(n)+1):
    if(n//i==i):
        c+=1
    else:
        c+=2
print(c)
if(c==2):
    print('prime')
else:
    print('not prime')
'''
#3.
'''
a=int(input())
p,np=0,0
for i in range(a):
    n=int(input())
    c=0
    for i in range(1,m.isqrt(n)+1):
        if(n%i==0):
            if(n//i==i):
                c+=1
            else:
                c+=2
    if(c%2!=0):
        print(c,'perfect square')
        p+=1
    elif(c==2):
        print(c,'non perfect square')
        print('prime')
        np+=1
    else:
        print(c,'non perfect square')
        np+=1
print('perfect square:',p,'non perfect square:',np)
'''
#4.prime numbnners in given range
'''
n=int(input())
l=int(input())
p,np=0,0
for i in range(n,l+1):
    c=0
    for j in range(2,m.isqrt(i)+1):
        if(i%j==0):
            c+=1
            break
    if(c==0):
        print(i,'prime')
        p+=1
    else:
        print(i,'not prime')
        np+=1
print(p,np)
'''
#5.
'''
n=int(input())
x=n
mi=99999
ma=0
p,np=0,0
while(x>0):
    a=x%10
    c=0
    for j in range(1,m.isqrt(a)+1):
        if(a%j==0):
            if(a//j==j):
                c+=1
            else:
                c+=2
    if(c==2):
        p+=1
        if(mi>a):
            mi=a
    else:
        np+=1
        if(ma<a):
            ma=a
    x//=10
f=1
for k in range(1,ma+1):
    f*=k
print('highest not prime factorial',f)
f=1
for k in range(1,mi+1):
    f*=k
print('lowest prime factorial',f)
print('prime',p,'non prime',np)
'''
#6.
'''
n=int(input())
s=0
a,b=0,1
for i in range(n):
    print(a,end=' ')
    s+=a
    c=a+b
    a=b
    b=c
print(s)
'''
#7.

n=int(input())
a,b,d,s=int(input()),int(input()),int(input()),0
for i in range(n):
    print(a,end=' ')
    s+=a
    c=a+b+d
    a=b
    b=d
    d=c
print(s)

#8.gcd of given number
'''
n1,n2=map(int,input().split())
while(1):
    a=n2%n1
    if(a==0):
        print(n1)
        break
    n2=n1
    n1=a
'''
#9.lcm
'''
a,b=map(int,input().split())
g=0
while(1):
    r=b%a
    if(r==0):
        g=a
        break
    b=a
    a=r
print('lcm',int((a*b)/g))
'''
#collection
'''
l=[[4,3,6],[3,1,16],[2,5,7],[1,6,4]]
l.sort(key=lambda a:a[1])
print(l)
'''
