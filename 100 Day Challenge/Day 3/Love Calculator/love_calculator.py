# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

#Counts each letter per name and adds them together
t = lower_case_name1.count("t") + lower_case_name2.count("t")
r = lower_case_name1.count("r") + lower_case_name2.count("r")
u = lower_case_name1.count("u") + lower_case_name2.count("u")
e = lower_case_name1.count("e") + lower_case_name2.count("e")
l = lower_case_name1.count("l") + lower_case_name2.count("l")
o = lower_case_name1.count("o") + lower_case_name2.count("o")
v = lower_case_name1.count("v") + lower_case_name2.count("v")

#Adds the total for each letter together
true = t + r + u + e
love = l + o + v + e

love_score_str = str(true) + str(love)
love_score_int = int(love_score_str)

#If your score less than 10 or greater than 90
if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")

#If your score is greater than or equal to 40 or less than equal to 50
elif love_score_int >= 40 and love_score_int <= 50:
    print(f"Your score is {love_score_int}, you are alright together.")

#Else score
else:
    print(f"Your score is {love_score_int}.")