#Nested Lists

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomoatoes", "Celery", "Potatoes"]

fruits = ["Strawberries","Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomoatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

#Prints whole list
print(dirty_dozen)

#Prints nested list
print(dirty_dozen[0])
print(dirty_dozen[1])

#Prints item from specified nested list
print(dirty_dozen[1][3])