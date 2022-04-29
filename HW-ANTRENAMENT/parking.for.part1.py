PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if FREE_PLACE != place_index:
        print("| X |", end="")
    else:
        print("|   |", end="")
print("\n","#"*PARKING_PLACES*5, sep="") #sep="" -> separator/spatiu

