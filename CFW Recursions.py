# power of a number using recursion
'''
def pow(n, p):
    if p == 0:
        return 1
    else:
        return n*pow(n, p-1)


n = int(input('abse'))
p = int(input('powee'))
print(pow(n, p))
'''
# print all natural numbers from 1 to n using recursion
'''
def print_n(n):
    if n == 0:
        return
    print_n(n-1)
    print(n)
n = int(input('enter n'))
print_n(n)  
'''
# print even or odd numbers in given range using recursion
'''
def print_even_odd(n, m, even=True):
    if n > m:
        return
    if even:
        if n % 2 == 0:
            print(n)
    else:
        if n % 2 != 0:
            print(n)
    print_even_odd(n+1, m, even)    
n = int(input('enter n'))
m = int(input('enter m'))
print_even_odd(n, m, even=True)
print_even_odd(n, m, even=False)
'''
# sum of even number in given range using recursion
'''
def sum_e(n,m):
    if n>m:
        return 0
    if n%2==0:
        return n+sum_e(n+1,m)  
    else:
        return sum_e(n+1,m)  
n=int(input('enter n'))     
m=int(input('enter m'))
print(sum_e(n,m))
'''
