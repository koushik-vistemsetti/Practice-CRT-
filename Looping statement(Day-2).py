# if n=5 generate 2 4 8 16 32
'''
n=int(input())
for i in range(1,n+1):
    print(2**i,end=' ')
'''
#if n=6 op 5,7,9,11,13,15
'''
n=int(input())
a=5
for i in range(1,n+1):
    print(a,end=" ")
    a+=2
'''
#6  65 66 67 68 69 70
'''
a,n=65,int(input())
for i in range(1,n+1):
    print(a,end=" ")
    a+=1
'''
# 6 97 99 101 103 105 107
'''
a,n=97,int(input())
for i in range(1,n+1):
    print(a,end=" ")
    a+=2
'''
#n=4 *$@
'''
n=int(input())
for i in range(n):
    print("*$@")
'''
#n=4 AZ BY CX DW
'''
n=int(input())
for i in range(n):
    print(chr(65+i),chr(90-i))
'''
#n=4 aA bB cC dD
'''
n=int(input())
for i in range(n):
    print(chr(97+i),chr(65+i))
'''
#r=5,c=4 box of *
'''
r,c=map(int,input().split())
for i in range(c):
    for j in range(r):
        print("*",end=' ')
    print()
'''
#n=m=3 $@ $@ $@ || *1 *2 *3.....
'''
n=int(input())
for i in range(n*2):
    for j in range(n):
       if i%2==0:
           print("$@",end='  ')
       else:
           print("*",j+1,end='  ')
    print()
'''
#r=3 c=5 1 2 3 4 5 ||6 7 8 9 10.....
'''
r,c=map(int,input().split())
for i in range(r):
    for j in range(c):
        print((c*i)+(j+1),end=' ')
    print()
'''
#n=4 ****@||***@@||**@@@....
'''
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("* ",end=' ')
    for j in range(i+1):
        print('@',end=' ')
    print()

#or
n=int(input())
for i in range(n):
    for j in range(n+1):
        if(i+j<n):
            print('* ',end=' ')
        else:
            print('@',end=' ')
    print()
'''
# in book
'''
n=int(input())
for i in range(n):
    print(n-i,end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
'''
#74928 op 28,92,49,74,7 op 928,492,749
'''
import math as m
n=74928
while n>0:
    a=n%100
    n=n//10
    print(a,end=',')
print()
n=74928
while n>0:
    a=n%1000
    n=n//10
    d=m.log10(a)+1
    if(d>3):
        print(a,end=',')
'''
#1.count even digit in number
'''
n=int(input())
e=0
while n>0:
    a=n%10
    if(a%2==0):
        e+=1
    n=n//10
print(e)
'''
#2,3.reverse and palindrome
'''
n=int(input())
p=n
s=0
while(n>0):
    a=n%10
    s=(s*10)+a
    n//=10
print("Reverse number:",s)
if(p==s):
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
#4.even postion even number odd positioin odd number
import math as m
n=int(input())
p=1
c=0
while n > 0:
    d=int(m.log10(n))
    a=n//(10**d)
    if p%2==0:
        if a%p==0:
            c+=1
    else:
        if a%2!=0:
            c+=1
    p+=1
    n=n%(10 ** d)
print(c)
    


    
    
