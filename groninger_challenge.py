
"""
a.Not a Triangle (a+b<c) 
b.A right triangle 
c. an obtuse tirangle
d. an acute triangle
"""

a=float(input("Please give me a length for a triangle: "))

b=float(input("Please give me another length: "))

c=float(input("Please give me a hypotenuse: "))

if (a+b < c):
    print ("That's not a Triangle, silly goose!")

elif (a**2 + b**2 ==c**2):
    print ("That's a right triangle!")
    
elif (a**2 + b**2 <c**2):
    print ("That's an Obtuse Triangle!")
    
elif ((a**2 + b**2 >c**2) + (a+b > c)):
    print ("That's an Acute Triangle!")