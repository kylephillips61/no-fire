# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:46:13 2016

Group project #7
Will, Bill, Kyle, Antoan

@author: S01007893
"""
import math

d = float(input("Please enter the diameter of your pipe: "))
r = d/2
h = float(input( "Please enter the length of you pipe: "))
print ("")

def perimeter():
    per = (r*2 * math.pi)
    return per
    
def area ():
    cap = (math.pi * (r**2))
    return cap
    
def volume ():
    vol = (area() * h)
    return vol
    
def surfaceArea ():
    surf = (perimeter() * h)
    return surf
        
def main():
    result1 = perimeter()
    result2 = area()
    result3 = volume ()
    result4 = surfaceArea ()
    print("The perimeter is", result1)
    print("The area is", result2)
    print("The volume is", result3)
    print("The surface area is", result4)
    print("")

main()    

while True:
    x = input("Would you like to run it again? ")
    if  x == "yes":
       d = float(input("Please enter the diameter of your pipe: "))
       r = d/2
       h = float(input( "Please enter the length of you pipe: "))
       print("")
       main()
   
    elif x == "no":
       break
   
    else:
        print("Input is incorrect! Try again.")
    
print("Finished")