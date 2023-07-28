import numpy as np
from PIL import Image

width, height = 600, 800

img = np.zeros((height, width,3), dtype=np.uint8)

# draw background
img[ : ] = (91, 158, 225 )
img[int (height*0.85):height, 0:width] =  (22, 69, 46 )

# draw building
img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (118, 68, 138 )

# draw windows
for row in range(6):
    for column in range(5):
        if np.random.randint(0,8) == 5:
            window_color =   (199, 227, 225)
        else:
            window_color =   (252, 243, 207 )
        img[
            int(height*0.1 + 100*row  + 20):int(height*0.1 +100*row  + 60 +20),
            int(width*0.2 + 75*column + 15): int(width*0.2 + 75*column + 30 +15)
            ] = window_color 

# save image
Image.fromarray(img).save( "Building.png")

