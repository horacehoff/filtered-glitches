from PIL import ImageEnhance, Image, ImageFilter
from os import listdir
import os
from os.path import isfile, join
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
def nft(file):
    print ("\033[A                                                     \033[A")
    print("--------------------------\nFILTERED GLITCHES NFT GENERATOR\nBy @Just_a_Mango\n--------------------------")
    print("Starting nft generation for '"+file+"'...")
    enhancer = ImageEnhance.Sharpness(Image.open(file))
    print("Starting image sharpening...")
    enhancer = enhancer.enhance(50000)
    im1 = enhancer.filter(ImageFilter.SHARPEN)
    print("Image sharpening finished")
    print("Starting image sharpening...")
    import random
    index = random.randint(5,5000)
    i = 0
    while i < index:
        im1 = im1.filter(ImageFilter.SHARPEN)
        print ("\033[A                             \033[A")
        print("Image sharpening -> "+str(i)+" out of "+str(index)+" | "+str(round(((i*100)/index), 2))+"%")
        i = i+1
    i = 0
    import random
    index = random.randint(5,5000)
    while i < index:
        im1 = im1.filter(ImageFilter.BLUR)
        print ("\033[A                             \033[A")
        print("[SECOND PASS]Image sharpening -> "+str(i)+" out of "+str(index)+" | "+str(round(((i*100)/index), 2))+"%")
        i = i+1
    number = random.randint(1, 1000)
    print("Saving first image... -> "+"outimg"+str(number)+".png")
    im1.save("Images/outimg"+str(number)+".png")
    print("Starting image 'bluring'...")
    index = random.randint(5,5000)
    i = 0
    im2 = im1
    while i < index:
        im2 = im2.filter(ImageFilter.SHARPEN)
        print ("\033[A                             \033[A")
        print("Image 'blur' -> "+str(i)+" out of "+str(index)+" | "+str(round(((i*100)/index), 2))+"%")
        i = i+1
    number = random.randint(1, 1000)
    print("Saving second image... -> "+"outimg"+str(number)+".png")
    im2.save("Images/outimg"+str(number)+".png")
    
while True:
    img_path = input("Desired image path: ")
    if os.path.isfile(img_path):
        nft(img_path)
        break
    else:
        print ("\033[A                                                     \033[A")
        pass