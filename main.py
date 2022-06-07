"""
# Q.1) To find the largest number between 2 numbers.
num1 = input("What's the fist number: ")
num2 = input("What's the second number: ")
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")
=================================================
# Q.2) To find the largest number between 3 numbers.
num1 = input("What's the fist number: ")
num2 = input("What's the second number: ")
num3 = input("What's the third number: ")
if (num1 > num2) and (num1 > num3):
    print(f"{num1} is larger than {num2} and {num3}.")
elif num2 > num3:
    print(f"{num2} is larger than {num1} and {num3}.")
else:
    print(f"{num3} is larger than {num2} and {num1}.")
========================================================
# Q.3) To check whether a number is negative, positive or zero
num = int(input("Enter the number that you want to check: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num == 0:
    print(f"It's a zero.")
else:
    print(f"{num} is a negative number.")
===============================================
# Q.4) To check whether a number is divisible by 5 or not (or just check divisibility
# of any two numbers):
num1 = int(input("Enter the number that you want to check: "))
num2 = int(input("Enter the number that you want to check divisibility with: "))
if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")
===================================================
# Q.5) To check if the given number is odd or even
num = int(input("Enter the number that you want to check: "))
if num % 2 == 0:
    print(f"{num} is even number.")
else:
    print(f"{num} is odd number.")
======================================================
# Q.6) TO check whether a year is leap year or not:
year = int(input("Enter Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
================================================
# Q.7) To check if whether a character is alphabet or not.
char = input("Enter the character: ")
if char.isalpha():
    print(f"{char} is an alphabet character.")
else:
    print(f"{char} is not an alphabet character.")
====================================================
# Q.8) To check if whether an alphabet character is vowel or constant.
char = input("Enter the character: ").lower()
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"{char} is a vowel in an alphabet.")
else:
    print(f"{char} is a constant in an alphabet.")
===================================================
# Q.9) To check if character is uppercase or lowercase:
char = input("Enter the character: ")
if char.islower():
    print(f"{char} is a lowercase alphabet.")
else:
    print(f"{char} is a uppercase alphabet.")
====================================
# Q.10) To count total number of notes in given amount.
amount = int(input("How much amount you want to calculate: "))
value_of_note = int(input("What is the value of single note: "))
num_of_notes = int(amount / value_of_note)
verify_amount = num_of_notes * value_of_note
if amount == verify_amount:
    print(f"You have {num_of_notes} notes of {value_of_note} value and total amount is {amount} INR.")
else:
    print(f"Please enter right amount and value of single note.")
========================================================
# Q.11) To check if whether the triangle is valid or not by using given angles:
a1 = int(input("Enter value of first angle of a triangle: "))
a2 = int(input("Enter value of second angle of a triangle: "))
a3 = int(input("Enter value of third angle of a triangle: "))
if a1 + a2 + a3 == 180:
    print(f"{a1, a2, a3} are angles of valid triangle.")
else:
    print(f"{a1, a2, a3} these angles are not sides of a valid triangle.")
=======================================================
# Q.12) To check if whether the triangle is valid or not by using given sides:
s1 = int(input("Enter value of first side of a triangle: "))
s2 = int(input("Enter value of second side of a triangle: "))
s3 = int(input("Enter value of third side of a triangle: "))
if (s1 + s2 > s3) and (s1 + s3 > s2) and (s3 + s2 > s1):
    print(f"{s1, s2, s3} are sides of valid triangle.")
else:
    print(f"{s1, s2, s3} these sides are not sides of a valid triangle.")
===============================================
# Q.13) To check whether a triangle is Equilateral or Isosceles or Scalene Triangle:
s1 = int(input("Enter value of first side of a triangle: "))
s2 = int(input("Enter value of second side of a triangle: "))
s3 = int(input("Enter value of third side of a triangle: "))
if (s1 + s2 > s3) and (s1 + s3 > s2) and (s3 + s2 > s1):
    print(f"{s1, s2, s3} are sides of valid triangle.")
    if s1 == s2 == s3:
        print("It's a Equilateral triangle.")
    elif (s1 == s2) or (s1 == s3) or (s2 == s3):
        print("It's an  Isosceles triangle.")
    else:
        print("It's a Scalene Triangle.")
else:
    print(f"{s1, s2, s3} these sides are not sides of a valid triangle.")
=====================================================
# q. Reverse the words:Altaf Malgan
s = 'Altaf Malgan'
for i in s.split()[::-1]:
    print(i,end=' ')
==========================================
# Interview q. i want a dict of each block and its count
#  {'A':1,'m':1,'i':1,'t':1,'a':3.....}
s = 'Amitabh Bachchan'
d = {}
for i in s:
    #print(i,s.count(i))
    # d[key] = value
    d[i] = s.count(i)
print(d)
=========================
# while loop
# Q1 all natural numbers from 1 to n.
i = 1
while (i<=100):
    print(i)
    i+=1
==============================
# while loop
# Q2 all natural numbers from 1 to n. revers order
number = int(input("please enter any number: "))
i = number
print("List of natural numbers from{0}to 1 in revers order:".format (number))
while(i>=1):
    print(i, end = '')
    i = i - 1
==========================================
# Q3.print all alphabets from a to z using while loop.
import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end='')
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end='')
====================================================
"""



