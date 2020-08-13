import glob
import PIL
from PIL import Image, ImageEnhance
#use pillow-simd
import numpy as np
import cv2
import os
import random

class test(object):
    #idk why object is there tbh from SO
    def __init__(self):
        #ranges to be adjusted
        r0= random.randint(0,10)
        r1= random.randint(0,10)
        r2= random.randint(0,10)
        r3= random.randint(0,10)
        r4= random.randint(0,10)

    def alpha(self,r0,r1,r2,r3,r4):
        #UNFINISHED
        print (r0,r1,r2,r3,r4)
        z = 0
        factor = -1000
        x = ((z),'.png')
        images = glob.glob("mask/*.png")
        images2 = glob.glob("hands/*.png")
        for image,image2 in zip(images, images2):
        	x = ((z),'.png')
        	img2 = Image.open(image2)
        	img = Image.open(image)
        	enhancer = ImageEnhance.Brightness(img2)
        	img2 = enhancer.enhance(factor)
        	img2 = img2.resize([512,512],PIL.Image.NEAREST)
        	img.paste(img2, (0,0), img2)
        	img.save(image.split('/')[1])
        	z = (z) + 1
        	print("ALPHA#:", (z),"/",len(images))

    def super(self,r0,r1,r2,r3,r4):
        #UNFINISHED
        print (r0,r1,r2,r3,r4)
        zz = 0
        xx = ((zz),'.png')
        imagesr = glob.glob("faces/*.jpg")
        images2r = glob.glob("hands/*.png")
        for imager,image2r in zip(imagesr, images2r):
        	img = cv2.imread(imager, -1)
        	img2 = cv2.imread(image2r, -1)
        	h, w, c = img2r.shape
        	result = np.zeros((h, w, 3), np.uint8)
        	xx = ((zz),'.png')
        	img2r = cv2.resize(img2r,(1024,1024), interpolation = cv2.INTER_LINEAR)
        	alpha = np.tile(img2r[..., 3][..., None], 3) / 255.0
        	result = (1. - alpha) * imgr[..., :3] + alpha * img2r[..., :3]
        	cv2.imwrite(imager.split('/')[1],result)
        	zz = (zz) + 1
        	print("FACE#:", (zz),"/",len(imagesr))
