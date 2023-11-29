"""
-------------------------------------------------------
[Building a Guessing Game]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

# created string variable
secret_word = "giraffe"

# created guess variable
guess = ""

# guess count
count = 0

# guess limit
limit = 3

# tells if they have more guesses left
# should be false to start the loop  and for else it is True
out_of_guesses = False

# while guess is not equal to secret word keep looping
while guess != secret_word and not (out_of_guesses):
    if count < limit:
        # ask for their input in the while loop
        guess = input("Enter guess: ")
        # count of guesses increasing
        count += 1
    else:
        # if they ran out of guesses they lose
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
print()
print("You win!")
