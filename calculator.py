#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:17:59 2021

@author: chaitanyasudarsan
"""
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
# For selecting the following arthemetic operation

print("1-Addition, 2- Subtraction, 3- Multiplication, 4-Division")

operation = float(input("Select the arthemetic operation 1/2/3/4: "))
 # 1- addition
 # 2- subtraction
 # 3- multiplication
 # 4- division
if operation == 1:
    print(float(num1 + num2))
elif operation == 2:
    print(float(num1 - num2))
elif operation == 3:
    print (float(num1 * num2))
elif operation ==4:
    print(float(num1 / num2))
else:
 print("you didnt choose the right operation")

