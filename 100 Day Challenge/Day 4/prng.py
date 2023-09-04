#Psuedo Random Number Generator

#Imports the random module
import random

#Generates a random integer between 1 and 10 inclusive
random_interger = random.randint(1, 10)
print(random_interger)

#Generates a random float number between 0 and 1 exlusive
#Multiplying the variable can increase the range of float numbers generated
random_float = random.random() * 5
print(random_float)