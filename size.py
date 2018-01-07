#!/usr/bin/env python

#random number
import random
#image library pillow
import PIL

numbo = open('num')
iparsed = PIL.ImageFile.Parser()
closing = iparsed.close()
# gpio values
lights = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def stop():
    closing.save("post.jpg")
    numbo.close()

if lights not in numbo
    stop()

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
