# Problem 4: While Loop Game

# Guessing Game

secret_number = 7
number_of_guesses = 0

while True:
    # Changing the prompt based on the number of guesses
    if number_of_guesses == 0:
        print("Welcome to the Guessing Game!")
        guess = int(input("Guess a number:  "))
    elif number_of_guesses < 10:
        guess = int(input("Come on! Guess a number:  "))
    else:
        guess = int(input("Is your guessing skills so poor? Try again:  "))
    
    number_of_guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {number_of_guesses} tries.")
        break

# End of the game
