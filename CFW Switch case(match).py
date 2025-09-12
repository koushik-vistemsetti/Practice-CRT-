#1.day in a week using switch case
week = int(input("Enter week number (1-7): "))
match week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter week number between 1-7.")

#2.program to print number of days in a month using switch case
n=int(input())
match n:
    case 1|3|5|7|8|10|12:
        print(31)
    case 4|6|9|11:
        print(30)
    case 2:
        print(28)
    case _:
        print("Enter Valid month number")

#3.vowel or consonent using switch
ch = input("Enter any alphabet: ")

match ch:
    case 'a':
        print("Vowel")
    case 'e':
        print("Vowel")
    case 'i':
        print("Vowel")
    case 'o':
        print("Vowel")
    case 'u':
        print("Vowel")
    case 'A':
        print("Vowel")
    case 'U':
        print("Vowel")
    case 'I':
        print("Vowel")
    case 'O':
        print("Vowel")
    case 'U':
        print("Vowel")
    case _:
        print("Consonant")

#4.find maximum between two numbers using switch case.
m,n=map(int,input().split())
match (m>n):
	case True:
		print(m)
	case False:
		print(n)

#5.check whether a number is even or odd using switch case.

n=int(input())
match n%2==0:
	case True:
		print("Even")
	case False:
		print("Odd")



#6.check whether a number is positive, negative or zero using switch case.
n=int(input())
match n>0:
	case 0:
		print("Zero")
	case True:
		print("Positive")
	case False:
		print("Negetive")

#7.program to find all roots of a quadratic equation using switch case
import math as m
a, b, c = map(int, input().split())
d = b**2 - 4*a*c
status = ("positive" if d > 0 else"zero" if d == 0 else"negative")
match status:
    case "positive":
        r1 = (-b + m.sqrt(d)) / (2*a)
        r2 = (-b - m.sqrt(d)) / (2*a)
        print(f"Two distinct and real roots exist:\nRoot1: {r1:.2f}\nRoot2: {r2:.2f}")
    case "zero":
        r1 = r2 = -b / (2*a)
        print(f"Two equal and real roots exist:\nRoot1: {r1:.2f}\nRoot2: {r2:.2f}")
    case "negative":
        real = -b / (2*a)
        imag = m.sqrt(-d) / (2*a)
        print(f"Two distinct complex roots exist:\nRoot1: {real:.2f} + {imag:.2f}i\nRoot2: {real:.2f} - {imag:.2f}i")

#8.create Simple Calculator using switch case.
m,n=map(int,input().split())
op=input()
match op:
	case '+':
		print(f"sum={m+n}")
	case '-':
		print(f"sub={m-n}")
	case '*':
		print(f"mul={m*n}")
	case '/':
		print(f"div={m/n}")
	case '%':
		print(f"mod={m%n}")
	case _:
		print("Invalid")

