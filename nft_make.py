from PIL import ImageEnhance, Image, ImageFilter
from os import listdir
import os
from os.path import isfile, join
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
for file in onlyfiles:
    i = [1, 2]
    for x in i:
        enhancer = ImageEnhance.Sharpness(Image.open(file))
        enhancer = enhancer.enhance(50000)
        im1 = enhancer.filter(ImageFilter.SHARPEN)
        import random
        index = random.randint(5,5000)
        i = 0
        while i < index:
            im1 = im1.filter(ImageFilter.SHARPEN)
            i = i+1
        i = 0
        import random
        index = random.randint(5,5000)
        while i < index:
            im1 = im1.filter(ImageFilter.BLUR)
            i = i+1
        if (bool(random.getrandbits(1)) == True):
            index = random.randint(5,5000)
            i = 0
            im2 = im1
            while i < index:
                im2 = im1.filter(ImageFilter.SHARPEN)
                i = i+1
        im1.save("Out/outimg"+str(x)+str(random.randint(1, 1000))+".png")
        im2.save("Out/outimg"+str(x+55)+str(random.randint(1, 1000))+".png")