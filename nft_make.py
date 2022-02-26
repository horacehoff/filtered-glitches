from PIL import ImageEnhance, Image, ImageFilter
from os import listdir
import os, getopt, sys
from os.path import isfile, join
def nft(file):
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
        index = random.randint(5,5000)
        i = 0
        im2 = im1
        while i < index:
            im2 = im2.filter(ImageFilter.SHARPEN)
            i = i+1
        im1.save("Images/outimg"+str(x)+str(random.randint(1, 1000))+".png")
        im2.save("Images/outimg"+str(x+55)+str(random.randint(1, 1000))+".png")
        
argumentList = sys.argv[1:]
options = "i:cd"
long_options = ["CheckInstall", "InputFile =", "Debug"]
arguments, values = getopt.getopt(argumentList, options, long_options)
if arguments:
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--InputFile"):
            nft(currentValue)