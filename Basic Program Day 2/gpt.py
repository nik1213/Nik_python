A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
D = int(input("Enter the fourth number: "))
E = int(input("Enter the fifth number: "))

greatest = A

if B > greatest:
    greatest = B
if C > greatest:
    greatest = C
if D > greatest:
    greatest = D
if E > greatest:
    greatest = E

print(greatest, "is the greatest number")