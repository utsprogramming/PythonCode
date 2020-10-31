# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:24:39 2020

@author: areez

Ask for user input for 5 different numbers.
 1 has to be a float, 1 has to be an integer,
 and the rest can be up to you. Add these numbers to a list.
 Then take 3 numbers from your list and run an if statement to determine whether the number should be printed or not. 

"""
a = int(input("Number1="))
b = float(input("Number2="))
c = input("Number3=")
d = int(input("Number4="))
e = int(input("Number5="))

List = [a,b,c,d,e]

if a or d or e == int():
    print (List[0], List[3], List[4])
