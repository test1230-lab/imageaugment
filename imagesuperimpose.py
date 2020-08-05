import glob
import numpy as np
import cv2

z = 0
x = ((z),'.png')
images = glob.glob("faces/*.jpg")
images2 = glob.glob("hands/*.png")
for image,image2 in zip(images, images2):
	img = cv2.imread(image, -1)
	img2 = cv2.imread(image2, -1)
	h, w, c = img2.shape
	result = np.zeros((h, w, 3), np.uint8)
	x = ((z),'.png')
	img2 = cv2.resize(img2,(1024,1024), interpolation = cv2.INTER_CUBIC)
	alpha = np.tile(img2[..., 3][..., None], 3) / 255.0
	result = (1. - alpha) * img[..., :3] + alpha * img2[..., :3]
	cv2.imwrite(image.split('/')[1],result)
	z = (z) + 1
	print("IMAGE:", (z),"/",len(images))
