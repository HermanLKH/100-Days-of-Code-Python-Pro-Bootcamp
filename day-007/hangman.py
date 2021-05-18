import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You already guessed '{guess}'")
  else:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose...")
        print(f"It's {chosen_word.upper()}")

    if "_" not in display:
      end_of_game = True
      print("You win!")
      
    print(stages[lives])