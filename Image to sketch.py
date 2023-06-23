import numpy as np 
import imageio 
import cv2 i
mport scipy.nd image

img="image1. jpg" #replace with your desired image file name
def grayscale(rgb):
  return np.dot [...,:3], [0.299,0.587,0.114])
  
def dodge(front, back):
  result=front*255/(255-back)
  result [result>255]=255
  result [back==255]=255
  return result. astype( 'uint8')
  
S=imageio.imread(img)
g=grayscale(s)
i=255-g

b=scipy.nd image.filters.gaussian_filter(i,sigma=10)
r=dodge (b,g)
