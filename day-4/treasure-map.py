# Treasure map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row_index = int(position[1]) - 1
column_index = int(position[0]) - 1

map[row_index][column_index] = 'x'

print(f"{row1}\n{row2}\n{row3}")