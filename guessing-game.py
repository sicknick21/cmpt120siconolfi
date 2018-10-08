#guessing-game.py
#Program that allows the user to guess the name of an animal.

import random
animal = {'lion','tiger','bear' ,'owl','frog','toucan','monkey', 'shark', 'zebra', 'wolverine', 'dog', 'cat', 'gorilla', 'fish', 'fox', 'groundhog',}

randomanimal = random.choice(dict(enumerate(animal)))
guess = ""
print ("This program is thinking of an animal.")

while guess != randomanimal:

    if guess != "":
        print ("Your guess is wrong, try again.")

    guess = input('What animal is the program thinking of?')

print ("Congratulations, you win!")
