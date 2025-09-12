import math as m
#1.
'''
n=int(input())
s=0
d=m.log10(n)+1
while n>10:
    a=n%100
    n=n//10
    s+=a
print(s)
'''
#2.
'''
n=int(input())
s=1
while n>0:
    a=n%10
    n=n//10
    s*=a
print(s)
'''
#3.
'''
n=int(input())
s=1
while n>0:
    a=n%1000
    n=n//100
    s*=a
print(s)
'''
#sample

#4.
'''
n=int(input())
s=0
for i in range(n+1):
    s+=i
print(s)
'''
#5.
'''
n=int(input())
s=1
for i in range(1,n+1):
    s*=i
print(s)
'''
#conversionss
#6.
'''
n=int(input('number'))
g=int(input('given base'))
d=int(input('desired base'))
x=n
c,p,s,q,r=0,0,0,0,0
while(x>0):
        if(g<=x%10):
            print('Invalid')
            c+=1
        x//=10
if(c==0 and (d==10 or g==10)):
    while(n>0):
            s+=((n%d)*(g**p))
            n//=d
            p+=1
    print(s)
elif(c==0 and (d!=10 and g!=10)):
    while(n>0):
            s+=((n%10)*(g**p))
            n//=10
            p+=1
    while(s>0):
            q+=((s%d)*(10**r))
            s//=d
            r+=1
    print(q)
'''
#7.
'''
n=int(input('number'))
x,d,p,r,s,s1,q=n,0,0,0,0,0,0
while(x>0):
    if(d<(x%10)):
        d=x%10
    x//=10
while(n>0):
            s+=((n%d)*(10**p))
            n//=d
            p+=1
x=s
while(x>0):
    r=r*10+x%10
    x//=10
while(r>0):
            s1+=((r%10)*(d**q))
            r//=10
            q+=1
print(s1)
'''
#8.
'''
n=int(input())
s1=0
while n>0:
    s=1
    a=n%10
    for i in range(1,a+1):
        s*=i
    n//=10
    s1+=s
print(s1)
'''
#9.
'''
n=int(input())
s=0
while n>10:
    r=0
    a=n%100
    n=n//10
    while(a>0):
        r=r*10+a%10
        a//=10
    s+=r
print(s)
'''
#10.
n=int(input())
d=int(m.log10(n))+1
m=0
mi=999999
r=0
for i in range(1,d+1):
    if(i%2!=0):
        r=r*10+n%10
    n//=10
while(r>0):
    if(m<(r%10)):
        m=r%10
    if(mi>r%10):
        mi=r%10
    r//=10
print(m,mi)
f=0
s=1
for i in range(1,m+1):
    s*=i
print(s)
f+=s
s=1
for i in range(1,mi+1):
    s*=i
f+=s
print(s)
print(f)

    


            


    

    
    
