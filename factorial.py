# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 06:14:18 2018

@author: SAN
""" 


# Python program to find the factorial of a number provided by the user. 
 
 
 # to take input from the user 
num = int(input("Enter a number: ")) 
  
 
  factorial = 1 
  
 
  # check if the number is negative, positive or zero 
  if num < 0: 
     print("Sorry, factorial does not exist for negative numbers") 
  elif num == 0: 
     print("The factorial of 0 is 1") 
  else: 
     for i in range(1,num + 1): 
         factorial = factorial*i 
     print("The factorial of ",num," is ",factorial) 
