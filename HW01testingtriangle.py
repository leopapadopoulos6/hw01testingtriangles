"""
Leonidas Papadopoulos
HW01: Testing Triangle classification
"""
import unittest
#defining the correct properties of a triangle
#The sum of the length of any two sides of a triangle is greater than the length of the third side.
def valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

#classifying each type of triangle.
def classify_triangle(a,b,c):
    if a==b==c:
        print("equilateral")
        return 'equilateral'
    elif a==b or b==c:
        print("isoceles")
        return 'isoceles'
    elif a ** 2 + b **2 == c **2:
        print("right")
        return 'right'
    else:
        print("scalene")
        return 'scalene'
#user input for the lengh of each side
a = float(input("Side a length: "))
b = float(input("Side b length: "))
c = float(input("Side c length: "))

if valid_triangle(a,b,c):
    classify_triangle(a,b,c)
else:
    print("Please try again. The sides you entered do not form a triangle")
    print("Hint: The sum of the length of any two sides of a triangle is greater than the length of the third side.")


