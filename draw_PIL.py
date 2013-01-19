from PIL import Image, ImageDraw
import math

import pandas as pd
import random
import time

random.seed(time.time())

# my_data = np.genfromtxt('ish.csv', delimiter=',')
# nn = len(my_data)
# my_data = my_data.tolist()

image=Image.new("RGB",(200,200),(255,255,255))
pic=ImageDraw.Draw(image)

t = 0.0
for _ in xrange(5000):
    t += 0.1
    try:
        x = int(t * math.cos(t) + 100.0)
        y = int(t * math.sin(t) + 100.0)
        pic.line((x, y, x, y), fill=(255,0,255))
    except:
        continue

image.save('lg.png', 'PNG')
