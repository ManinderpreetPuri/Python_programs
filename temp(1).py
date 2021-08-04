# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Task 1:
# =============================================================================
# Minimum of Two Numbers: Write a program that reads two integers and prints out 
# the Minimum

fn = int(input('Enter first number ='))
sn = int(input('Enter second number ='))
area = int(1/4 * 3.14 * dia * dia)
volume = area * height
print('The volume of diameter=', dia,'and height=', height,'can is ', volume,'.')
 
# =============================================================================
# =============================================================================

#Task 2
# Write a Python program to calculate the body mass index (BMI) value. The program 
# reads weight in kilograms and height in centimetres. The program then calculates the 
# body mass index (BMI) value using the following formula:
# - BMI= weight in kilograms / (height in meters)^2
# 
# Display the volume using formatted print.

weight = float(input('Weight of person in kg is= '))
height = float(input('Height of person in cm is= '))
height_in_meters = float(height/100)
height_in_meters_sq =  height_in_meters * height_in_meters  
BMI = weight / height_in_meters_sq
print('The BMI of the person is ', BMI)

# =============================================================================
# =============================================================================

#Task 3
# Write a Python program to read time in minutes from user and then convert them into 
# days, hours and minutes. Display the days, hours and minutes using formatted print.
# Use the following formulas for time conversion (note % is the modulus operator): 
# - MINUTES_IN_DAY = 24 * 60
# - days = time / MINUTES_IN_DAY
# - time_Left = time % MINUTES_IN_DAY
# - hours = time_Left / 60
# - minutes = time_Left % 60
# For example, if we key in 173420 minutes, we will get days: 120, hours: 10, minutes: 
# 20.

MINUTES_IN_DAY = 24 * 60
time = int(input('Minutes = '))
days_Left = int(time/MINUTES_IN_DAY)
minutes_Left = time % MINUTES_IN_DAY
hours_Left = int(minutes_Left / 60)
minutes = minutes_Left % 60
print('Time left is : ','days =',days_Left,'hours =', hours_Left, 'minutes =', minutes)
 
# =============================================================================
# =============================================================================

#Task 4
# You run 10 kilometres in 40 minutes 30 seconds. Write a Python program to find out 
# how many miles you can run in an hour. A mile is 1.61 kilometres.
# - time = minutes * 60 + seconds
# - Number of kms run in 1 hour = kilometres / time * 3600
# - number of miles run in 1 hour= Number of kms run in 1 hour / 1.609
# For this example, the speed (in miles per hour): 9.173491362011196

dis = float(input('Distance covered in kms = '))
hours = int(input('Hours spent to cover distance = '))
minutes = int(input('Minutes spent to cover distance = '))
seconds = int(input('Seconds spent to cover distance = '))
time = hours * 60 * 60 + minutes * 60 + seconds
No_kms_in_1_hour = dis / time * 3600
No_miles_in_hour = No_kms_in_1_hour / 1.609
print('Number of kms run in an hour = ', No_kms_in_1_hour)
print('Number of miles run in an hour = ', No_miles_in_hour)

# =============================================================================
# =============================================================================

#Task 5
#  Write a Python program to calculate the minimum number of tables required for a group
# of diners. Assume that each table has 8 seats (one size only). Ask the user for the size
# of the table and the group. A sample execution of the program is
# - Enter the table size: 8
# - Enter the number of diners: 15
# - Number of tables to book: 2

import math
table_size = int(input('Enter the table size= '))
number_diners= int(input('Enter the number of diners= '))
number_of_tables = number_diners / table_size
print('Number of tables to book = ',math.ceil(number_of_tables))

# =============================================================================
# =============================================================================

# Task 6
#  Write a Python program to calculate the minimum number of tables required for a group
# of diners. Assume that each table has 8 seats (one size only). Ask the user for the size
# of the table and the group. A sample execution of the program is
# - Enter the table size: 8
# - Enter the number of diners: 15
# - Number of tables to book: 2

import math
numb_comp = int(input('Number of computers = '))
cable_length = int(input('Cable length required in cms to secure a computer = '))
roll_length = int(input('Roll length in metres = '))
total_cable_length_req_incms = numb_comp * cable_length
rolls_length_incms =  roll_length * 100
number_rolls = total_cable_length_req_incms / rolls_length_incms
print('Number of rolls needed = ', math.ceil(number_rolls))
 
# =============================================================================
# =============================================================================
 
# Task 7
# Write a Python program to calculate the minimum number of tables required for a group
# of diners. Assume that each table has 8 seats (one size only). Ask the user for the size
# of the table and the group. A sample execution of the program is
# - Enter the table size: 8
# - Enter the number of diners: 15
# - Number of tables to book: 2

adults = int(input('Number of adults: '))
child = int(input('Number of children: '))
if adults >= 2 and child >=2:
        if adults % 2 == 0 and child % 2 == 0:    
            if adults < child:
                a = adults
                family_tick = a / 2 
                child_tick =  child - family_tick * 2 
                total_cost = family_tick * 26 + child_tick * 5
                print('Number of family tickets: ',int(family_tick))
                print('Number of adult tickets: ', 0)
                print('Number of child tickets: ',int(child_tick))
                print('Total cost = $',int(total_cost))
            else:
                a = child
                family_tick = a / 2 
                adult_tick = adults - family_tick * 2
                total_cost = family_tick * 26 + adult_tick * 10 
                print('Number of family tickets: ',int(family_tick))
                print('Number of adult tickets: ',int(adult_tick))
                print('Number of child tickets: ', 0)
                print('Total cost = $',int(total_cost))
        else:
            if adults < child:
                a = adults
                b = a % 2
                c = a - b
                adult_tick = b
                family_tick = c / 2
                child_tick = child - family_tick * 2
                total_cost = family_tick * 26 + adult_tick * 10 + child_tick * 5
                print('Number of family tickets: ',int(family_tick))
                print('Number of adult tickets: ', int(adult_tick))
                print('Number of child tickets: ',int(child_tick))
                print('Total cost = $',int(total_cost))
            else:
                a = child
                b = a % 2 
                c = a - b
                child_tick = b
                family_tick = c / 2
                adult_tick = adults - family_tick * 2
                total_cost = family_tick * 26 + adult_tick * 10 + child_tick * 5
                print('Number of family tickets: ',int(family_tick))
                print('Number of adult tickets: ',int(adult_tick))
                print('Number of child tickets: ', int(child_tick))
                print('Total cost = $',int(total_cost))
else :
        adult_tick = adults
        child_tick = child
        total_cost = adult_tick * 10 + child_tick * 5
        print('Number of family tickets: ',0)
        print('Number of adult tickets: ',int(adult_tick))
        print('Number of child tickets: ', int(child_tick))
        print('Total cost = $',int(total_cost))
        
