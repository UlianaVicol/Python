# x ----- R ------>
# 0 1 2 3 4 5 6 7 8 9


batteryCharge = 70   # %
retePerStep   = 10   # 10% / m

steps = 0
# COMPLEXITY
# DRY - Don't Repeat Yourself
while batteryCharge > 0:
######## one step ###############
    steps += 1 # increment
    batteryCharge  -= retePerStep # decrement
    print( "Steps:", steps, "baterry", batteryCharge, "%" )
    if batteryCharge <= 10:
        print("WARNING! NEED TO CGARGE" )
######## one step ###############
