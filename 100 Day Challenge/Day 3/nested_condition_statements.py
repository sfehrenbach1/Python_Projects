#Sample nested if else conditional

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5

    elif age >= 12 and age <= 18:
        print("Youth tickets are $7.")
        bill = 7

    elif age >=45 and age <= 55:
        print("You get a free ticket.")

    else:
        print("Adult tickets are $12. ")
        bill = 12

    wants_photo = input("Do you want your photo taken? ")
    
    if wants_photo == "Y" or "y" or "Yes" or "yes":
    #Add $3 to bill
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")