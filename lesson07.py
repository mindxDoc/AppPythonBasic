import random

guesses_taken = 0
number_to_guess = random.randint(1,20)

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Take a guess: "))
    guesses_taken += 1

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {guesses_taken} attempts!")
        break
