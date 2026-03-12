# write python program to develop a calculator
A=float(input("Enter the first number: "))
B=input("Enter the operation you need to perform ie. +,-,*,/:  ")
C=float(input("Enter the second number: "))

match B:
    case "+":
        print(A+C)
    case "-":
        print(A-C)
    case "*":
        print(A*C)
    case "/":
        print(A/C)
