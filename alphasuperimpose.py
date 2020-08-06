import glob
from PIL import Image, ImageEnhance
import PIL
#use pillow-simd
import time

z = 0
#factor will be changed to -1000, this is to just verify results
factor = -1000
x = ((z),'.png')
images = glob.glob("mask/*.png")
images2 = glob.glob("hands/*.png")
for image,image2 in zip(images, images2):
	t0 = time.perf_counter()
	x = ((z),'.png')
	img2 = Image.open(image2)
	img = Image.open(image)
	enhancer = ImageEnhance.Brightness(img2)
	img2 = enhancer.enhance(factor)
	img2 = img2.resize([512,512],PIL.Image.NEAREST)
	img.paste(img2, (0,0), img2)
	y = str(x)
	img.save(image.split('/')[1])
	z = (z) + 1
	#print("IMAGE:", (z),"/",len(images))
	t1 = time.perf_counter()
	print(t1-t0)
