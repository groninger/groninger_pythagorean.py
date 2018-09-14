"""
Write a program that will ask the user to enter their name and respond with a greeting using this name

"""

name=input("What is your name? ")
print ("Nice to meet you, " + name)

a=float(input("Please give me a length for a triangle: "))

b=float(input("Please give me another length: "))


print ("That means the hypotenuse is " + str((a**2 + b**2)**.5))
