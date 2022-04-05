PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "4321"

pin_door_1 = input("Enter first pin:")
lock_1_open = pin_door_1 == PIN_DOOR_1 # bool

if lock_1_open:
    print("I'm in the Building")

    pin_door_2 = input("Enter second pin:")
    lock_2_open = pin_door_2 == PIN_DOOR_2 # bool

if lock_2_open:
    print("I'm in the Flat")

#HW1: add else message