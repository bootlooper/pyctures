#!/usr/bin/env python

#random number
import random
#image library pillow
import PIL

numbo = open('num')
iparsed = PIL.ImageFile.Parser()
closing = iparsed.close()

# image size ideas
size0 = iparsed.open('size0.jpg')
size1 = iparsed.open('size1.jpg')
size2 = iparsed.open('size2.jpg')
size3 = iparsed.open('size3.jpg')

# gpio values
lights = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def stop():
    closing.save("post.jpg")
    numbo.close()

if __name__ == '__main__':
#    if numbo is:
#        size1.open()
    source = iparsed.open('size(random.randint(0,5)).jpg')
    size = PIL.Image.size(source)
    Image.transform(size, extent, data=None, 
nearest, fill=1, fillcolor=(random(000000, FFFFFF)))

    elif numbo not in main:
        stop()
