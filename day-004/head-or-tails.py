# Head or Tails

import random

random_side = random.randint(0, 1)
guess_side = input("Heads or Tails?\n")

if random_side == 1:
	result_side = "Heads"
else:
	result_side = "Tails"

if guess_side == result_side:
	print(f"You win! It's {result_side}")
else:
	print(f"You lose... It's {result_side}")