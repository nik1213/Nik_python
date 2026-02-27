''' We will try to print result in grade system for the user.
and the formula used will be 
percentage : (sum of marks/no of subject) *100
and based upon CGPA we will show grade to the user '''
import math

Maths= int(input(" Enter your marks scored in Maths : "))
Hindi= int(input(" Enter your marks scored in Hindi : "))
SST= int(input(" Enter your marks scored in SST : "))
Physics= int(input(" Enter your marks scored in Physics : "))
Bio= int(input(" Enter your marks scored in Bio : "))

Percent= (( Maths+Hindi+SST+Physics+Bio)/500)*100
if Percent >=90:
    G=1
elif Percent >= 80 and Percent<90:
    G=2
elif Percent >=70 and Percent<80:
    G=3
else :
    G=4
    
match G:
    case  1:
        print("your marks Percentage is ",Percent)
        print (" You Scored Good, A+")
    case  2:
        print("your marks Percentage is ",Percent)
        print("Good you got A in grade")
    case 3:
        print("your marks Percentage is ",Percent)
        print("You are OK, got a B in grade")
    case  4:
        print("your marks Percentage is ",Percent)
        print(" You are Fail, Go and Study ")


        
    
