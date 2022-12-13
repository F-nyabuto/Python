


import random
secret_words=open("secret.txt","r").readlines()
secret_words=random.choice(secret_words)
secret_words = secret_words[0:-1]
attempts = len(secret_words)
print(f"You have {attempts} attempts left!")
guess = input("Make a guess: ")
matching =[]
list_of_guesses = []
while True:
    list_of_guesses.append(guess)
    if guess == secret_words:
        print(f"You found the word. It was '{secret_words}'")
        break

    for letter in guess:
        if letter in secret_words:
            matching.append(letter)
    print(f"Your guess list of guesses {list_of_guesses}")

    for letter in secret_words:
        if letter in guess:
            print(letter, end="")
        else:
            print("-", end="")



    attempts -= 1
    if attempts == 0:
        print(f"\nGame over! The word was {secret_words}")
        break
    print(f"\nYou have {attempts} guesses left")
    guess = input("\nGuess: ")

    list_of_guesses.append(guess)
    if len(matching) == (len(secret_words)-1):
        print(f"You found the word. It was '{secret_words}'")
        break

# print(matching)
# print(secret_words)
