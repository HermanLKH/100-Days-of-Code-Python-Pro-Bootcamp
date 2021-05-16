import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 1st way
selected_name = random.choice(names)
# 2nd way
selected_name = names[random.randint(0, len(names) - 1)]

print(f"{selected_name} is going to buy the meal today!")