import random
from TheDice import *


def dice():
    faces = [1, 2, 3, 4,  5, 6]
    roll = random.choice(faces)
    if roll == 1:
        one()
    elif roll == 2:
        two()
    elif roll == 3:
        three()
    elif roll == 4:
        four()
    elif roll == 5:
        five()
    else:
        six()


while True:
    condition = input("You gonna roll the dice Buddy? <Y/N> ")
    if condition.lower() == "y" or condition.lower() == "n":
        if condition.lower() == "n":
            print("Ok, See ya...")
            break
        dice()
    else:
        print("Invalid input buddy")

