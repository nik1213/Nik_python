#Find the factorial of a given number 15
'''
To compute factorial:

Start with result = 1

Multiply result by 1

Multiply result by 2

Multiply result by 3

Keep multiplying until 15

Final result is 15!
-----------------------------------------------
Here is a clean point-wise explanation for this program

Definition: Factorial of a number n is the product of all positive integers from 1 to n.

Mathematical Formula: N!=N*(N-1)*(N-2)..........2*1
First we have taken a variable and initialised it and the value is as 1

R=1
now to find factorial we use for loop while is executed till 15th from 1

R=R*n
'''
#------------------------------------------


n=15
R=1
for n in range(1,16):
    R=R*n
    
print(R)

#========================================While loop------------------------------------------
'''
n=1
R=1
while n<16:
    R=R*n
    n=n+1
print(R)

'''