# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 05:42:06 2018

@author: SAN
"""

  # Python Program to find the L.C.M. of two input number 
  
 
  # define a function 
  def lcm(x, y): 
     """This function takes two 
     integers and returns the L.C.M.""" 
  
 
     # choose the greater number 
     if x > y: 
         greater = x 
     else: 
         greater = y 
  
 
     while(True): 
         if((greater % x == 0) and (greater % y == 0)): 
             lcm = greater 
             break 
         greater += 1 
  
 
     return lcm 
  
 
  # the following lines to take input from the user 
  num1 = int(input("Enter first number: ")) 
  num2 = int(input("Enter second number: ")) 
  
 
  print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)) 
