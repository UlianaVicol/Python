# this Module contains the MAP logical

# GAME MAP - matrix

# 0 - empty
# 1 - wall
# 2 - robo
rr = 5
rc = 9


gameMap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # 0 
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1], 
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1], 
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
   # 0  1                       9
]

gameMap[rr][rc] = 2 # put the robot in the specified coords


def p(c):
    print(c + " ", end="")

def printMap(m):
    for ri in range(10):
        for ci in range(10):
            if m[ri][ci] == 0:
                p(".")
            if m[ri][ci] == 1:
                p("⚔")
            if m[ri][ci] == 2:
                p("♔")
        print()