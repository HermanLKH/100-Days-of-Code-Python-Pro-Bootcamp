print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_num = int(input("How many people to split the bill? "))

tip_as_points = tip / 100
bill_with_tip = bill + bill * tip_as_points
bill_per_person = bill_with_tip / people_num

# 1st way
# bill_per_person = round(bill_per_person, 2)
# print(f"Each person should pay: ${bill_per_person}")

# 2nd way
print("Each person should pay: $" + "{:.2f}".format(bill_per_person))