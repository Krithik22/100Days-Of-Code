#Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int((input("What percentage of tip would you like to give? 10, 12 or 15? ")))
bill += bill*tip/100
tot_people = int(input("How many people to split the bill? "))
share = round(bill/tot_people,2)
print(f"Each person should pay ${share}")