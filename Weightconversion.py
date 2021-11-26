#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:04:14 2021

@author: chaitanyasudarsan
"""
Weight = float(input("Weight:")) 
unit = input("in(K)gs or (L)bs :")

if unit.upper() == "K":
     converted = Weight / 0.45
     print(" Weight in Lbs:" + str(converted))
     

else:
    converted = Weight * 0.45
    print("Weight in Kgs:" + str(converted))