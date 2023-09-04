# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)

#Generates random number between 0 and last index
random_name = random.randint(0, num_items - 1)

#Uses the random number generated to find the item in the list associated with that number
pays_bill = names[random_name]

#Prints who is paying the bill
print(f"{pays_bill} is going to buy the meal today!")