import cv2
from PIL import Image, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io
from skimage.color import rgb2gray
#matplotlib inline


#open the image as a PIL.Image.Image object and gray scale it
img1 = Image.open(r'C:\Users\Yael\Desktop\final project\Image processing\PC3\PC3_Glucose_1.tif').convert('LA')
# brightness the image so I can see the cells
enhancer = ImageEnhance.Brightness(img1)
# display the image
#img1.show()
'''
gray_r = enhancer.reshape(enhancer.shape[0]*enhancer.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(enhancer.shape[0],enhancer.shape[1])
plt.imshow(gray, cmap='gray')
'''