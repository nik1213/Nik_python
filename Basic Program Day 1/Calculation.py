#Take two numbers and print addition, subtraction, multiplication, division
A= float(input("Enter the first number :"))
B= float(input("Enter the second number :"))
Add= A+B
mul=A*B
if A>B:
    Sub=A-B
else:
    Sub=B-A
Div=A/B
print (" Addition of the given numbers are as :" ,Add)
print (" Subtraction of the given numbers are as :" ,Sub)
print (" Multiplication of the given numbers are as :" ,mul)
print (" Division of the given numbers are as :" ,Div)