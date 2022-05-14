from map import printMap, gameMap, rr, rc
from ui import *

while True:
    clear()
    printMap(gameMap)
    key = controls()

    if key == "x":
        break
    gameMap[rr][rc] = 0 
   
    if key == "d" and rc != 9 and gameMap[rr][rc+1] != 1:
        rc +=1      
        
    if key == "a" and rc != 0 and gameMap[rr][rc-1] != 1:
        rc -=1    
        
    if key == "s" and rr != 9 and gameMap[rr+1][rc] != 1: 
        rr +=1
    
    if key == "w" and rr != 0 and gameMap[rr-1][rc] != 1:
        rr -=1
    gameMap[rr][rc] = 2 


#HW1: add Up/Down movement
# HW2: boundaries check right -> 0, left - 0
# HW3: add some mines,
#      when moving right -> radar -> rc+1, rc+2 - not a mine
#      in case of danger -> warning -> danger detected