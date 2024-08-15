import matplotlib.image as image
import cv2

img=cv2.imread('grayscale.jpg')
a = cv2.resize(img, (128,128))
print('The Shape of the image is:',img.shape)
print('The image as array is:')
print(a)