# In the following we create a nested list
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


#Determine the position of treasure "X"
coordinator1 = int(position[1])
coordinator2 = int(position[0])
map[coordinator1-1][coordinator2-1] = "X"

# print the output to show the location of the treasure 
print(f"{row1}\n{row2}\n{row3}")
