#take day number(1 to 7) input from user and tell the day
# use of match case

Day=int(input("Enter the Day number to find the Day: "))

match Day:
    case 1: 
        print("Monday")
    case 2:
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
