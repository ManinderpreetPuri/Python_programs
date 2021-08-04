# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Task 1:
# Minimum of Two Numbers: Write a program that reads two integers and prints out 
# the Minimum

fn = float(input('Enter first number = '))
sn = float(input('Enter second number = '))
if fn < sn:
    print('The smallest number is : {}'.format(fn))
else:
    print('The smallest number is : {}'.format(sn))
 
# =============================================================================

#Task 2
#  Maximum of Three Numbers: Write a program that reads three integers and prints 
# out the maximum of the three.

fn = float(input('Enter first number = '))
sn = float(input('Enter second number = '))
tn = float(input('Enter third number = '))
if fn > sn and fn > tn:
    print('The largest number is : {}'.format(fn))
elif tn > sn and tn > sn:
    print('The largest number is : {}'.format(tn))
else:
    print('The largest number is : {}'.format(sn))

# =============================================================================

#Task 3
#  Sorting Three Numbers: Write a program that reads three integers and prints them out 
# in increasing order.

fn = int(input('Enter first number = '))
sn = int(input('Enter second number = '))
tn = int(input('Enter third number = '))
if fn > sn and sn > tn:
    print('The numbers in increasing order are : {} {} {}'.format(tn, sn, fn))
elif fn > tn and tn > sn:
    print('The numbers in increasing order are : {} {} {}'.format(sn, tn, fn))
elif sn > fn and fn > tn:
    print('The numbers in increasing order are : {} {} {}'.format(tn, fn, sn))
elif sn > tn and tn > fn:
    print('The numbers in increasing order are : {} {} {}'.format(fn, tn, sn))
elif tn > sn and sn > fn:
    print('The numbers in increasing order are : {} {} {}'.format(fn, sn, tn))
else:
    print('The numbers in increasing order are : {} {} {}'.format(sn, fn, tn))

# =============================================================================

#Task 4
#  Are numbers Strictly Ordered?: Write a program that reads three numbers and prints 
# “increasing” if they are in increasing order, “decreasing” if they are in decreasing, and 
# “neither” otherwise. We will take “increasing” to mean “strictly increasing”, with each 
# value larger than its predecessor. For example, the sequence 3 4 4 would not be 
# considered increasing.

fn = int(input('Enter first number = '))
sn = int(input('Enter second number = '))
tn = int(input('Enter third number = '))
if fn > sn and sn > tn:
     print('The numbers are in decreasing order.')
elif fn < sn and sn < tn:
     print('The numbers are in increasing order.')
else:
     print('The numbers are neither in increasing or decreasing order.')

# =============================================================================

#Task 5
#  Write a program that reads three numbers and prints “all the same” 
# if they are all the same, “all different” if they are all different, and “neither” otherwise.
 
fn = int(input('Enter first number = '))
sn = int(input('Enter second number = '))
tn = int(input('Enter third number = '))
if fn == sn and sn == tn:
      print('The numbers are same.')
elif fn != sn and sn != tn:
      print('The numbers are different.')
else:
      print('The numbers are neither same or different.')

# =============================================================================

# Task 6
#  Three Sides of a Triangle: Write a program that prompts the user for three positive
# numbers and then determines if the numbers can be the three sides of a triangle. For 
# three positive numbers to be the sides of a triangle, none should be bigger than or equal
# to the sum of the other two.

fn = int(input('Enter first number = '))
sn = int(input('Enter second number = '))
tn = int(input('Enter third number = '))
if fn >= sn + tn:
      print('The numbers cannot be sides of a triangle.')
elif tn >= sn + fn:
      print('The numbers cannot be sides of a triangle.')
elif sn >= fn + tn:
      print('The numbers cannot be sides of a triangle.')
else:
      print('The numbers can be sides of a triangle.')

# =============================================================================
 
# Task 7
#  Input Validation for Triangle Problem: In the previous question, what will happen 
# to your program if the user enters numbers that are 0 or negative? Modify the previous 
# program to validate the inputs upfront.

fn = int(input('Enter first number = '))
sn = int(input('Enter second number = '))
tn = int(input('Enter third number = '))
if fn == 0 or sn ==0 or tn == 0:
    print('One of the number is zero or a negative value')
elif fn < 0 or sn < 0 or tn < 0:
    print('One of the number is zero or a negative value')
else:    
    if fn >= sn + tn:
        print('The numbers cannot be sides of a triangle.')
    elif tn >= sn + fn:
        print('The numbers cannot be sides of a triangle.')
    elif sn >= fn + tn:
        print('The numbers cannot be sides of a triangle.')
    else:
        print('The numbers can be sides of a triangle.')
        
#=============================================================================

#Task 8
#  Counting Digits: Write a program that reads a positive integer and prints out how many 
# digits it has by checking whether the number is >= 10, >=100, and so on. The program 
# prints out one of the following messages “The number has 1 digit”, “The number has 2 
# digits”, “The number has 3 digits”, “The number has 4 digits”, “The number has more 
# than 4 digits”

no = int(input('Enter number = '))
if no >= 0:
    if no <= 10 :
        print('The number has 1 digit')
    elif no <= 100:
        print('The number has 2 digit')
    elif no <= 1000:
        print('The number has 3 digit')
    elif no <= 10000:
        print('The number has 4 digit')
    else:
        print('The number has more than 4 digit')
else:
    print('Please enter a positive integer')
    
# =============================================================================
    
#Task 9
# - Egg Classification: Eggs that weigh less than 55 grams are graded as small. Eggs in 
# the range 55-65 are graded medium. Eggs over 65 grams are graded large. Write a 
# program that asks a user to enter the weight of an egg and prints out its grade.

egg_w = int(input('Enter egg weight in grams = '))
if egg_w > 0:
    if egg_w < 55 :
        print('Small size egg')
    elif egg_w >= 55 and egg_w <= 65:
        print('Medium size egg')
    else:
        print('Large size egg')
else:
    print('Please enter a valid egg weight!')
    
# =============================================================================

#Task 10 
# Employee’s Payment: Write a program to calculate the weekly payment for an 
# employee working at a store. Information about the employee includes:
# • the employee’s name (a string)
# • the hourly pay rate (a float)
# • the number of hours the employee worked in the week (a float)
# • the total sales for the week (a float).
# An employee is expected to sell at least $100 worth of goods in each hour they work. 
# If they sell on average more than $100 an hour, they receive a bonus. The pay is 
# calculated as the number of hours they worked multiplied by their hourly pay rate plus 
# the bonus if they are entitled to one. The bonus is 10% of the sales amount they made 
# above the expected sales amount based on $100 an hour. Test Cases:
# • hours = 20.0
# • rate = 15.45
# • total sales = 4600.90
# • pay = 569.09
# • hours = 10.0
# • rate = 20.00
# • total sales = 3000.00
# • pay = 400.00

name = str(input('The employee’s name = '))
rate = float(input('The hourly pay rate = '))
hours = float(input('The number of hours the employee worked in the week = '))
sales = float(input('The total sales for the week = '))
if sales / hours >= 100:
    above = sales - 100 * hours
    bonus = above / 10
    pay = hours * rate + bonus
    print('Pay of {} for this week is {}'. format(name, pay))
else:
    print('Pay of {} for this week is {} (No bonus! Sorry).'. format(name, hours * rate))

# =============================================================================

# Task 11
# Ordering Books: A university bookstore wants a program to determine the number of 
# copies it should order for a book. Experience has shown that sales depend largely on 
# whether the book is required as a prescribed textbook or merely recommended and 
# whether or not it has been used before. A new, required textbook will sell 90% of 
# prospective enrollment, but if it has been used before 65% will buy. Similarly, 40% 
# will buy newly recommended books, but just half that many buy a book that has been 
# used before. Write a program that asks the user for all the information required for a 
# book, including the prospective class enrollment, and prints out how many copies the 
# bookstore should order (assuming there is no left-over stock for the book)

enroll = int(input('Prospective enrolllment number = '))
req_b = str(input('Is it a required book (Type Y or N) = '))
rec_b = str(input('Is it a recommended book (Type Y or N) = '))
used_b = str(input('Is it a book used before (Type Y or N) = '))
if req_b == 'Y' and rec_b == 'Y':
    print('Invalid! cant be both a required and a recommended book')
elif req_b == 'Y' and used_b == 'N':
    order = enroll - enroll / 10
    print('Order {} copies of this book!'.format(round(order)))
elif req_b == 'Y' and used_b == 'Y':
    order = enroll / 100 * 65
    print('Order {} copies of this book!'.format(round(order)))
elif rec_b == 'Y' and used_b == 'N':
    order = enroll / 100 * 40 
    print('Order {} copies of this book!'.format(round(order)))    
elif rec_b == 'Y' and used_b == 'Y':
    order = enroll / 100 * 20 
    print('Order {} copies of this book!'.format(round(order)))
else:
    print('Please try again!')

