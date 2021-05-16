# Caeser Cipher

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""

	if shift_amount > 26:
		shift_amount %= 26

	if cipher_direction == "decode":
		shift_amount *= -1

	for char in start_text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text += char
		
	print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)
is_end = False

while not is_end:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

	if not direction == "encode" and not direction == "decode":
		print("Input Error")
	else:
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))

		caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

	is_repeat = input('Want to restart? ')

	if is_repeat == "yes":
		is_end = False
	else:
		is_end = True
else:
	print("Goodbye!")