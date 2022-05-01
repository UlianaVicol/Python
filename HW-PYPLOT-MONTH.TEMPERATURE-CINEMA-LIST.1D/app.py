# App preocess & visualize image 
# 10 x 10 pixels resolution

image_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, ],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],

]

from matplotlib import pyplot 
from random import randint
# blur
#for ri in range(8):
    #for ci in range(8):
        #print(image_data[ri][ci])
        #pixel = (image_data[ri][ci] + image_data[ri][ci+1] + image_data[ri+1][ci] + image_data[ri+1][ci+1]) / 4
        #image_data[ri][ci] = pixel

# add noise 
#for ri in range(9):
       #for ci in range(9):
           #if randint(1,100) == 1:
               #image_data[ri][ci] = 0.5

# scale
image_data_small = [
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
]
for ri in range(4):
    for ci in range(4):
        pixel = (image_data[ri*2][ci*2] + image_data[ri*2][ci*2+1] + image_data[ri*2+1][ci*2] + image_data[ri*2+1][ci*2+1]) / 4
        image_data_small[ri][ci] = pixel

pyplot.imshow(image_data_small, cmap='gray')
pyplot.show()