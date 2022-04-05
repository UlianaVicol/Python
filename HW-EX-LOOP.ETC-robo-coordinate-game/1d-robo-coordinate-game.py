# Step 3
# x---R---- :
# CONTROLS: "a" - left, "d" - right
from os import system

LENGTH = 20
roboX  = 5

direction = ""
# game loop
while  direction != "X":
    system("cls")
# ############# DROW THE MAP ################
    print("\n")   # + "\n"
    x = 1
    while x <= LENGTH:
        if x == roboX:
            print("R", end="")  # "\n"
        else:
            print("-", end="")  # "\n"
        x += 1
    print("\n") # + "\n"
# ############# DROW THE MAP ################

# ############# CONTROLS ################
    direction = input("dir(a/d) >>>")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1
# ############# CONTROLS ################
   