import random

# Text file to store secret words
secret = open("secret.txt", "a")
secret.close()

# Reading and selecting a random word from secret list
lines = open("secret.txt", "r").readlines()
secrete_1 = random.choice(lines)
no_of_attempts = len(secrete_1)
secret.close()

print(f"You have {no_of_attempts} attempts left!")
guess = input("Make a guess: ")
match = []
list_of_guess = []

while True:
    # checking if user guessed correctly
    list_of_guess.append(guess)
    if guess == secrete_1:
        print(f"You found the word. It was '{secrete_1}'")
        break

    # checking if letter in user guess matches any character in password and storing matched character to match list
    for letter in guess:
        if letter in secrete_1:
            match.append(letter)
    print(f"Your guess list of guesses {list_of_guess}")

    for letter in secrete_1:
        if letter in guess:
            print(letter, end="")
        else:
            print("-", end="")

    # decrementing user number of attempts

    no_of_attempts -= 1
    if no_of_attempts == 1:
        print(f"\nGame over! The word was {secrete_1}")
        break
    print(f"\nYou have {no_of_attempts} guesses) left")
    guess = input("\nGuess: ")
