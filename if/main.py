import random

guessed = False

words = ("meatball", "hamburger", "fries")

while guessed == False:
    randChoice = random.choice(words)
    choice = input(f"Please choose ONE of the items in the list: \n\n{words}:  ")
    print("")
    print("")

    if choice.lower() == randChoice:
        guessed = True
        print("Correct! You won!")
    else:
        print(f"You didnt guess the right word ;( \n\n The word was: {randChoice.capitalize()}")
