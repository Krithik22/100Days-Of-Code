row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# print(position[0])
row=int(position[0])-1
column=int(position[1])-1
map[column][row]='x'
print(f"{row1}\n{row2}\n{row3}")
