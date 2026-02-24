#Find the greatest number from the 5 number taken from user in input

A=int(input("Enter the first number: "))
B=int(input("Enter the Second number: "))
C=int(input("Enter the Third number: "))
D=int(input("Enter the fourth number: "))
E=int(input("Enter the fifth number: "))

if A>B and A>C and A>D and A>E:
    print(A, " Is the biggest number")
elif B>A and B>C and B>D and B>E:
    print(B,' Is the Biggest number')
elif C>A and C>B and C>D and C>E:
    print(C, ' Is gratest number')
elif D>A and D>B and D>C and D>E:
    print(D," Is the gratest number")
else:
    print(E,' Is the gratest number')