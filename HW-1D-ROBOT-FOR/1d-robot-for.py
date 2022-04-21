# REMAKE 1d robo game -> for loop

from os import system
from random import randint

LENGTH_X  = 15
LENGTH_Y  = 10
roboX     = randint(1, LENGTH_X-1)
roboY     = randint(1, LENGTH_Y-1)

bombX     = randint(1, LENGTH_X-1)
bombY     = randint(1, LENGTH_Y-1)

heartY    = randint(1, LENGTH_Y-1)
heartX    = randint(1, LENGTH_X-1)

pizzaX    = randint(1, LENGTH_X-1)
pizzaY    = randint(1, LENGTH_Y-1)

SCORE     = 0
roboHP    = 100
roboBT    = 100
option    = ""
# game loop
while True:
############################ DROW MAP ####################################
    system("cls")
    print("\n")
    
    for x in range(1,LENGTH_Y + 1):  # 1..10
        print("\n", end = " ")
        for y in range(1, LENGTH_X +1 ):

            if roboX == x and roboY == y:
                print("🤖", end=" ")
                if roboX == heartX and roboY == heartY:
                    heartX = randint(1, LENGTH_X-1)
                    heartY = randint(1, LENGTH_Y-1)  
                    if roboHP < 100:
                        roboHP += 10
                        SCORE += 10  
            elif heartX == x and heartY == y:
                print("💛", end=" ")

            if roboX == bombX and roboY == bombY:
                if roboHP > 0 and roboHP <= 100:
                    roboHP -= 10
                    SCORE  -= 10
                else:
                    print("OOPS!!! ")
                    exit()    
                if roboX == bombX and roboY == bombY:
                    bombX = randint(1, LENGTH_X-1)
                    bombY = randint(1, LENGTH_Y-1)     
            elif bombX == x and bombY == y:
                print("💣", end=" ")
            
            # robo and pizza Mania :D
            if roboX == pizzaX and roboY == pizzaY :
                if roboHP > 0 and roboHP <= 100:
                    SCORE += 10  
                if roboX == pizzaX and roboY == pizzaY:
                    pizzaX = randint(1, LENGTH_X-1)
                    pizzaY = randint(1, LENGTH_Y-1)
                else:
                    print("GAME OVER! ")
                    print("Thank you for playing!")
                    
            elif pizzaX == x and pizzaY == y:
                print("🍕", end=" ")
            else:
                print(".", end=" ")       
    print("\n")
    print(f"HP: {roboHP}  SCORE: {SCORE}")
    
############################ DROW MAP ####################################

############################ 2. READ INPUT ####################################
    option = input(">>>").lower()
############################ 2. READ INPUT ####################################

############################ 3. DECIDE ####################################
    if option == "a" and roboX != 1:
        roboX-=1
    if option == "u" and roboX != LENGTH_X:
        roboX+=1
    if option == "d" and roboY != LENGTH_Y:
        roboY+=1
    if option == "w" and roboY > 1:
        roboY-=1

############################ 3. DECIDE ####################################


