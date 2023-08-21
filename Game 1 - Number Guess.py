import random
import math

# Selecting inputs
print("\n\tPick a range of numbers. Enter the lowest value.\n")
lower = int(input("Enter lower bound:- "))
print("\n\tGreat. Now enter the highest value.\n")
upper = int(input("Enter upper bound:- "))

# Selecting random number
x = random.randint(lower, upper)
print("\n\tI have now selected a number within " + str(lower) + " and " + str(upper) + "!")

# Game begins
print("\n\tYou have only", round(math.log(upper - lower + 1, 2)), "chances from your first guess to find the number! \n")

# Initializing number of guesses
count = 0

# for calculating the minimum number of guesses
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x, "better luck next time!")

while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number as an input
    guess = int(input("Guess a number:-"))

    # condition testing
    if x == guess:
        print("Congratulations, you did it in ", count, " attempts.")
        # once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")
# if guessing is more than required guesses, show this output: