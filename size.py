#!/usr/bin/env python

#random number
import random
#image library pillow
from PIL import Image, ImageDraw

numbo = open('num.log', 'w')

#hex 16 number
rando = hex(random.randint(0,15))
numbo.write(rando)



#close num.log, EOF
numbo.close()

#if int{1, 3, 5, 13, 15}:
#    im = Image.open(phonebase.jpg)
#elif int{2, 8, 9, 12}:
#    im = Image.open(1920x1200.jpg)
#elif int{4, 10, 11, 14}:
#    im = Image.open(1200x900.jpg)
#else:
#    end
