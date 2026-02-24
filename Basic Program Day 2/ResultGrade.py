#Take marks (0–100) and print grade (A/B/C/Fail)
# For A >=88
# for B : 88>B>=75
# for C : 75>C>=65
# less then 65 fail

Mark=float(input("Please Enter you Total Score to check Grade :"))

if Mark>=88:
    print("Hurrey!, You have got A")
elif Mark<88 and Mark>=75:
    print("Good, You Scored a B in your Exam. Best of Luck! for future")
elif Mark<75 and Mark >=65:
    Print("You got a C in you ecam, You need to work more in future")
else:
    print("your score is ",Mark, " Less then the required conditions to Pass, Hence you are FAIL. Please Prepare for Re-Test")
