from os import system
# LEGEND
# 0 -  FREE
# 1 - RESERVED
# 2 - BOUGHT
seats = [ 0, 0, 1, 2, 0, 0, 0, 0]
# index   0, 1, 2, 3, 4, 5, 6, 7

option = -1

while option !=0:
    # iterative count algorithm #####
    # HW1: let's say free_seats = len(seats)
    free_seats = len(seats)
    for pi in range ( len(seats) ):
        if seats[pi] == 1 or seats[pi] == 2:
            free_seats -= 1
    # ###############################


    ############# PLOT ###############
    system("cls")
    print()
    for pi in range( len(seats) ):
        print("", pi+1, "", end="  ")
    print()

    for pi in range( len(seats) ):
        if seats[pi] == 1:
            print("|-|", end="  ")
        elif seats[pi] == 2:
            print("|+|", end="  ")
        elif seats[pi] == 0:
            print("| |", end="  ") 
    print("\nFree seats: " ,free_seats)
    print("\n")

    ############### PLOT ##############

    # ### Show Menu ###################

    print("Menu")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("----------------")
    # #################################
    
    option = int(input(">>> "))
    if option <= 0 or option >= 3:
        system("cls")
    # HW2: add check condition :
    #      - boundaries 
    #      - check if the place is free     
                                                                                                                                                                                                                                
    if option == 1:
        place = int(input( "Wich place? " ))
        if seats[place-1] == 0:
            seats[place-1] = 1 
            system("cls")  
                 
        else:
            system("cls")
            print("Reserved or bought") 
    else:
        system("cls")
        print("error")                    
    # HW3: add buy, cancel + check ONLY if BOOKED!!!             
        if option == 2:
            place = int(input( "Wich place? " ))
            if seats[place-1] == 0:
                seats[place-1] = 2 
                system("cls")      
            else:
                system("cls")
                print("Reserved or bought")  
        else:
            system("cls")
            print("error")  
        if option == 3:
            place = int(input( "Wich place? " ))
            if seats[place-1] == 1:
                seats[place-1] = 0 
                system("cls")      
            else:
                system("cls")
                print("Reserved or bought")     
        else:
            system("cls")
            print("error")                                                      
                                              
                                     