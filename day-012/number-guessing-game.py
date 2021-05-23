import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

	if difficulty == "hard":
		return HARD_LEVEL_TURNS
	else:
		return EASY_LEVEL_TURNS

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number_of_attempts = set_difficulty()
answer = random.randint(1, 100)
guess = 0

while number_of_attempts > 0 and not guess == answer:
	print(f"You have {number_of_attempts} attempts remaining to guess the number.")

	guess = int(input("Make a guess: "))

	if guess == answer:
		print(f"You got it! The answer was {answer}.")
		break
	elif guess > answer:
		print("Too high.\nGuess again.")
	else:
		print("Too low.\nGuess again.")

	number_of_attempts -= 1
else:
	print(f"You've run out of guesses, you lose. It's {answer}")