# typical exemple
# APP -> memory -> task 

# CRUD / BREAD
from os import system
tasks = [] # empty list 
# MAIN LOOP ############################
while True:
    system("cls")
    print("=" * 20, "MENU", "=" * 20)
    print("0. Exit")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Count task")
    print("4. Change task")
    print("5. Remove task")
    print("6. Swap task")
    print("=" * 47)
    option = int(input(">> "))
    if option == 1:
        system("cls")
# ADD TASK ###############################
        while True:
            new_task = input("Name your next task:")
            if new_task == "":
                break
            if new_task not in tasks:
                tasks.append(new_task)
            else:
                print("Existing Task! Try again!")
    if option == 2:
        system("cls")  
# PRINT TASKS #############################
        print("\nYour tasks: ")
        for i in range(len(tasks)):

            print(i+1, " > ", tasks[i])
        input("\nHit Enter to continue")
# COUNT TASKS ###############################
    if option == 3:
        system("cls")
        print(f"Your list have {len(tasks)} tasks")
        input("\nHit Enter to continue")

    if option == 4:
        system("cls")
# EDIT A TASK ##############################
        index = int(input("Enter task position: ")) - 1
        if index <= len(tasks) and index >= 0:
            new_task = input(f"Enter task title <{tasks[index]}>: ")
            if new_task and new_task not in tasks:
                tasks[index] = new_task
                input("\nHit Enter to continue")       

    if option == 5:
        system("cls")
# REMOVE TASK ###############################
        index = int(input("Enter task position: ")) - 1
        if index <= len(tasks) and index >= 0:
            rem_task = input(f"Are you sure, you want to remove this task? : << tasks[index]?>>, \nyes/no:").lower()
            if rem_task[0] == "y":
                del tasks[index]
                print("Deleted task!")
                break
            else:
                break

    if option == 6:
        system("cls")
# SWAP TASKS ###########################
        indexA = int(input("Enter first task position: ")) - 1
        indexB = int(input("Enter second task position: ")) - 1
        tasks[indexB],tasks[indexA] = tasks[indexA],tasks[indexB]

# EXIT TASKS ###########################
    if option == 0:
        system("cls")
        break


# HW1: p. 3. -> task  for the index -> remove (look in python list methods)
#        * print the task title / confirm yes / no?
# HW2: +p.5 - swap taskA with taskB -> indexA, indexB
#           - additional variable (temp), triangle principle 
    
    
    
    