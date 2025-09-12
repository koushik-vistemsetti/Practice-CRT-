#1.Square Star Pattern
'''
n=int(input())#5
for i in range(n):
    for j in range(n):
        print('*',end=' ' )
    print()
'''
#2.Hollow Square with Diagonal
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n or j==n-i+1):
            print("*",end='')
        else:
            print("  ",end='')
    print(" ")
'''
#3.Right Triangle Star Pattern
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("* ",end=' ')
    print()
'''
#4.Hollow Right Triangle
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        if(j==0 or j==i or i==n-1):
            print("*",end=' ')
        else:
            print("  ",end=' ')
    print()
'''
#5.Mirrored Right Triangle
'''
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("   ",end=' ')
    for j in range(i+1):
        print("* ",end=' ')
    print()
'''
#6.Inverted Mirrored Right Triangle
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("   ",end=' ')
    for j in range(i,n-1):
        print("* ",end=' ')
    print()
'''
#7.Pyramid Star Pattern
'''
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("   ",end=' ')
    for j in range(i+1):
        print("* ",end=' ')
    for j in range(i):
        print("* ",end=' ')
    print()
'''
#8.Hollow Pyramid Star Pattern
'''
n = int(input())
for i in range(1, n+ 1):
    for j in range(i, n):
        print("   ", end="")
    for j in range(1, 2 * i):
        if i==n or j==1 or j==(2 * i - 1):
            print("* ", end="")
        else:
            print("   ", end="")
    print()
'''
#9.Diamond Star Pattern
'''
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("   ",end=' ')
    for j in range(i+1):
        print("* ",end=' ')
    for j in range(i):
        print("* ",end=' ')
    print()
for i in range(n-1):
    for j in range(i+2):
        print("   ",end=' ')
    for j in range(n-i-1):
        print("* ",end=' ')
    for j in range(n-i-2):
        print("* ",end=' ')
    print()
'''
#10.filled k star pattern
'''
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    for j in range(i+1):
        print("  ",end=' ')
    for j in range(i):
        print("  ",end=' ')
    print()
for i in range(n-1):
    for j in range(i+2):
        print("*",end=' ')
    for j in range(n-i-1):
        print("  ",end=' ')
    for j in range(n-i-2):
        print("  ",end=' ')
    print()
'''
