# OK 1. generate 2 random instagram accounts
# OK 2. print name, description and country
# OK 3. compare follower count
# OK 4. print game result
# OK 5. if win, let b = a, generate a new random instagram account, score += 1
# OK 6. if lose, show final score

import random
from art import logo, vs
from game_data import data

def higher_lower():
	score = 0
	guess_is_wrong = False

	a = random.choice(data)
	b = random.choice(data)
	
	while not guess_is_wrong:
		if a["follower_count"] > b["follower_count"]:
			answer = "A"
		else:
			answer = "B"

		print(logo)
		print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
		print(vs)
		print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')

		guess = input("Who has more followers? Type 'A' or 'B': ")

		if guess == answer:
			score += 1

			a = b
			b = random.choice(data)
		else:
			print(f"Sorry, that's wrong. Final score: {score}")
			guess_is_wrong = True

higher_lower()