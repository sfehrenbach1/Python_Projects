#Calculator to determine how much of a tip each person should leave on a bill

print("Welcome to the tip calculator.")

bill = float(input("What was the total of the bill? "))
total_people = int(input("How many people are splitting the bill? "))
tip_percentage = int(input("What percentage tip would you like to leave? 10, 12, or 15? "))

bill_with_tip = ((tip_percentage / 100) * bill) + bill
bill_per_person = bill_with_tip / total_people

rounded_bill = round(bill_per_person, 2)

print(f"Each person should pay ${rounded_bill}")