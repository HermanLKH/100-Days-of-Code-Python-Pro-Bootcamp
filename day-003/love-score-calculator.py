print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

num1 = 0
num2 = 0
names = name1 + name2

num1 += names.count("t")
num1 += names.count("r")
num1 += names.count("u")
num1 += names.count("e")

num2 += names.count("l")
num2 += names.count("o")
num2 += names.count("v")
num2 += names.count("e")

love_score = int(str(num1) + str(num2))

if love_score < 10 or love_score > 90:
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")