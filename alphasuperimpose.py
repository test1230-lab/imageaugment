import glob
from PIL import Image, ImageEnhance


print("the number of files in each dir must be the same")
z = 0
factor = 1000
x = ((z),'.png')
images = glob.glob("mask/*.jpg")
print ("number of files in dir mask:",len(images))
images2 = glob.glob("hands/*.png")
print ("number of files in dir hands:",len(images2))
for image,image2 in zip(images, images2):
    with open(image, 'rb') as file:
        with open(image2, 'rb') as file2:
            x = ((z),'.png')
            img2 = Image.open(file2)
            img2 = img2.enhance(factor)
            img = Image.open(file)
            img.paste(img2, (0,0), img2)
            y = str(x)
            img.save("{}.png".format(z))
            z = (z) + 1
            print("IMAGE:", (z),"/",len(images))
            
