print("Welcome to the tip calculator!\n")
total = int(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
noPeople = int(input("How many people to split the bill?"))

totalWithTip = total + (total * tip / 100) 

tipPerPerson = round((totalWithTip/noPeople),2)

match tip:
    case 10:
        print(f" Each person should pay {tipPerPerson}")
    case 12:
        print(f" Each person should pay {tipPerPerson}")
    case 15:
        print(f" Each person should pay {tipPerPerson}")

