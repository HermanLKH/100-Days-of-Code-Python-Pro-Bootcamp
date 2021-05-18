from art import logo
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

print(logo)

bids = {}

def bid():

	bidder = input("What's your name? ")
	bid = int(input("What's your bid? "))

	bids[bidder] = bid

def get_highest_bid():
	highest_bid = 0
	winner = ""

	for bidder in bids:
		bid = bids[bidder]

		if bid > highest_bid:
			winner = bidder
			highest_bid = bid
	
	print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bidding = True

while continue_bidding:
  bid()

  continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if continue_bidding == "yes":
    cls()
    continue_bidding = True
  else:
    continue_bidding = False
else:
  get_highest_bid()