import random
from art import logo

figures = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = '♠♥♣♦'
jqk10 = ['J', 'Q', 'K', '10']

def get_card(figure, suit):
	if figure == '10':
		return f'''
			┌───────┐
			| {figure}    |
			|       |
			|   {suit}   |
			|       |
			|    {figure} |
			└───────┘
		'''
	else:
		return f'''
			┌───────┐
			| {figure}     |
			|       |
			|   {suit}   |
			|       |
			|     {figure} |
			└───────┘
		'''

def init(player_type):
	return {
		"player_type": player_type,
		"figures": [],
		"suits": [],
		"images": [],
		"points": 0,
		"bust": False,
		"blackjack": False
	}

def pick(cards, number_of_card):
	while number_of_card > 0:
		card_figure = random.choice(figures)
		card_suit = random.choice(suits)

		card_image = get_card(card_figure, card_suit)

		cards["figures"].append(card_figure)
		cards["suits"].append(card_suit)
		cards["images"].append(card_image)
		number_of_card -= 1
	
	get_points(cards)

def pick_more(cards):
	if cards["player_type"] == "player":
		print("Here's your cards")
		for card_image in cards["images"]:
			print(card_image)

		while not cards["points"] > 21:
			is_pick_card = input("Type 'y' to get another card, type 'n' to pass:")
			if is_pick_card == "y":
				pick(cards, 1)
				for card_image in cards["images"]:
					print(card_image)

			else:
				break
	
	elif cards["player_type"] == "npc":
		while cards["points"] < 17:
			pick(cards, 1)
		print("Computer's first card")
		print(cards["images"][0])
	
	if cards["points"] > 21:
		cards["bust"] = True

def get_points(cards):
	cards["points"] = 0

	if len(cards["figures"]) == 2:
		for figure in jqk10:
			if figure in cards["figures"] and 'A' in cards["figures"]:
				cards["points"] = 21
				cards["blackjack"] = True
				return

	for figure in cards["figures"]:
		if figure in jqk10:
			cards["points"] += 10
		elif figure.isnumeric():
			cards["points"] += int(figure)

	for figure in cards["figures"]:
		if figure == 'A':
			if cards["points"] <= 10:
				cards["points"] += 11
			else:
				cards["points"] += 1

def get_game_result(player_cards, npc_cards): 
	print("Here's your opponent cards.")
	for card_image in npc_cards["images"]:
		print(card_image)

	print(f"Your final hand: {player_cards['points']}")
	print(f"Computer's final hand: {npc_cards['points']}")

	if not player_cards["bust"] and not npc_cards["bust"]:
		if player_cards["blackjack"]:
			print("You win with a Blackjack! 😎")
		elif npc_cards["blackjack"]:
			print("NPC wins with a Blackjack! 😱")
		elif player_cards["points"] > npc_cards["points"]:
			print("You win! 😃")
		elif player_cards["points"] < npc_cards["points"]:
			print("You lose 😤")
		else:
			print("IT's a tie! 🙃")
	elif player_cards["bust"] and not npc_cards["bust"]:
		print("You are bust... You lose 😤")

	elif not player_cards["bust"] and npc_cards["bust"]:
		print("You win! NPC bust! 😁")
	
	else:
		print("It's quite awkward... Both of you bust 🙄")

def play_game():
	print(logo)
	start_game = True
	
	while start_game:
		# Initial pick
		player_cards = init("player")
		npc_cards = init("npc")
		
		pick(player_cards, 2)
		pick(npc_cards, 2)

		pick_more(npc_cards)
		pick_more(player_cards)

		get_game_result(player_cards, npc_cards)

		playing_option = input("Do you want to play Blackjack? Type 'y' or 'n': ")
		
		if playing_option == "y":
			play_game()
		else:
			start_game = False
	else:
		print("Thank you for playing BlackJack! See u!😎")

play_game()