#1.program to find maximum between two numbers
'''
a,b=map(int,input().split())
print(a if(a>b) else b)
'''
#2.program to find maximum between three numbers
'''
a,b,c=map(int,input().split())
g=a if a>b and a>c else b if b>c else c
print("Greatest Number is :",g)
'''
#3.program to check whether a number is positive, negative or zero
'''
n=int(input())
print("Positive" if n>0 else "Negative" if n<0 else "Zero")
'''
#4.program to check whether a number is divisible by 5 and 11 or not
'''
n=int(input())
print("It is divisible by 5 & 11" if n%5==0 and n%11==0 else "Not divisible by 5 & 11")
'''
#5.program check whether a number is even or odd
'''
n=int(input())
print("Even" if n%2==0 else "Odd")
'''
#6.program to check Leap Year
'''
n=int(input())
print("Leap year" if n%4==0 and n%100!=0 or n%400==0 else "Non leap year")
'''
#7.program to check whether a character is alphabet or not
'''
c=input()
print("Alphabet" if (c>='a' and c<='z' or c>='A' and c<='Z') else "Not alphabet")
'''
#8.program to check vowel or consonant
'''
ch=input()
v='aeiouAEIOU'
print("Vowel" if ch in v else "Consonant")
'''
#9.program to check whether a character is alphabet, digit or special character
'''
ch=input()
print("Alphabet" if (ch>='a' and ch<='z' or ch>='A' and ch<='Z') else "Number" if ch>='0' and ch<='9' else "Special Character")
'''
#10.program to check whether a character is Uppercase or Lowercase
'''
c=input()
print("Lower case" if (c>='a' and c<='z' ) else "Upper case" if c>='A' and c<='Z' else "Not a Alphabet")
'''
#11.program to enter week number and print day of week
'''
n=int(input())
w=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
print(w[n-1])
'''
#12.program to find number of days in month
'''
n=int(input())
print(31 if (n in [1,3,5,7,8,10,12]) else 30 if n in [4,6,9,11] else 28)
'''
#13.program to count total number of notes in given amount
'''
n=int(input())
notes=[500,100,50,20,10,5,2,1]
print("Total notes")
for note in notes:
    c=n//note
    print(f"{note}:{c}")
    n%=note
'''
#14.program to check whether triangle is valid or not if angles are given
'''
a,b,c=map(int,input("angels of triangle").split())
print("Valid triangle" if a+b+c==180 and a!=0 and b!=0 and c!=0 else "Not a valid triangle")
'''
#15.program to check whether triangle is valid or not if sides are given
'''
a,b,c=map(int,input("Sides of triangle ").split())
print("Valid triangle" if a+b>c and b+c>a and c+a>b else"Not a valid triangle")
'''
#16.program to check whether triangle is equilateral, scalene or isosceles
'''
a,b,c=map(int,input("sides of triangle").split())
print("Equilateral Trinangle" if a==b==c else "Isoseceles Triangle" if a==b or b==c or c==a else "Scalene Triangle")
'''
#17.program to find all roots of a quadratic equation
'''
import math as m
a, b, c = map(int, input().split())
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + m.sqrt(d)) / (2*a)
    r2 = (-b - m.sqrt(d)) / (2*a)
    print(f"Two distinct and real roots exist:\nRoot1: {r1:.2f}\nRoot2: {r2:.2f}")
elif d == 0:
    r1 = r2 = -b / (2*a)
    print(f"Two equal and real roots exist:\nRoot1: {r1:.2f}\nRoot2: {r2:.2f}")
else:
    real = -b / (2*a)
    imag = m.sqrt(-d) / (2*a)
    print(f"Two distinct complex roots exist:\nRoot1: {real:.2f} + {imag:.2f}i\nRoot2: {real:.2f} - {imag:.2f}i")
'''
#18.program to calculate profit or loss
'''
cp = int(input())
sp = int(input())
print("Profit of" if sp > cp else "Loss of", abs(sp - cp))
'''
#19.program to enter student marks and find percentage and grade
'''
marks = list(map(float, input("5 subjects marks (space-separated): ").split()))
per= sum(marks) / 5
print(f"Per = {per:.2f}\nGrade {'A' if per >= 90 else 'B' if per >= 80 else 'C' if per>= 70 else 'D' if per>= 60 else 'E' if per >= 40 else 'F'}")
'''
#20.program to enter basic salary and calculate gross salary of an employee
'''
basic = float(input())
if basic <= 10000:
    hra = 0.20 * basic
    da = 0.80 * basic
elif basic <= 20000:
    hra = 0.25 * basic
    da = 0.90 * basic
else:
    hra = 0.30 * basic
    da = 0.95 * basic
gross = basic + hra + da
print(f"Gross salary = {gross:.0f}")
'''
#21.program to calculate electricity bill
'''
units= float(input())
bill = 0
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 50 * 0.50 + (units - 50) * 0.75
elif units <= 250:
    bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
sur = 0.20 * bill
total = bill + sur
print(f"Total  Bill = ₹{total:.2f}")
'''













      
