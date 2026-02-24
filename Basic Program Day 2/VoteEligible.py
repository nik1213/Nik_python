#Take age and check if eligible to vote (>=18)
import math

Name = str (input("Please enter you Name :"))
Age = int(input("Please enter you Age: "))

if Age>=18:
    print (Name, 'you are Eligible to Vote')
else:
    print(Name,'You are under age, Hence cannot vote')
