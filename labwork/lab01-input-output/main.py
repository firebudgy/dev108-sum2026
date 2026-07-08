# DEV 108 Lab Activity 1
# 7/6/2026
# Dragan Tuip

# Start writing your code below.
# Click the "Run" button (or run this file in the terminal with: python main.py)
# to see your output in the terminal window.
# Good luck! You can do this - please don't use any AI tools to do this assignment. 
# That violates the AI Policy for this class and puts your learning at a disadvantage. 

print("Hello, world!")
math1 = 5 * 5
print(math1)
math2 = 5 + 5 
print(math2)

firstName = "Dragan"
lastName = "Tuip"
major = "Information Technology"

print("My name is",firstName,lastName + ".")
print("My major is",major + ".")

num1 = float(input("Please type your first number, from 0 to 100:"))
num2 = float(input("Please type your second number, from 10 to 10000:"))
# It's been so long I spent like. 20 minutes trying to figure out why this doesn't work
# I forgot to use floats.
output = num1 * num2
print(num1,"*",num2,"=",output)
output2 = pow(num1,num2)

print(num1,"^",num2,"=",output2)