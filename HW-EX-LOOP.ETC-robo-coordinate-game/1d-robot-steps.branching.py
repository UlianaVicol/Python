# x ----- R ------>
# 0 1 2 3 4 5 6 7 8 9


batteryCharge = 70   # %
retePerStep   = 10   # 10% / m

steps = 0
steps = steps + 1

batteryCharge  = batteryCharge - retePerStep
print( "Steps:", steps, "baterry", batteryCharge, "%" )