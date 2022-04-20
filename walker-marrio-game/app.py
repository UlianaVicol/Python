import turtle as t
from lib import *

windowSetup(WIDTH,HEIGHT)
showMarrio(marrioX, 0)
showCoin(coinX)
showBomb(bombX)
showHeart(heartX)
t.listen()
t.onkey(moveRight, 'Right')
t.onkey(moveLeft, 'Left')

t.mainloop()