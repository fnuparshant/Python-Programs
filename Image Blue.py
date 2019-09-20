#name: Fnu Parshant
#Email: fnu.parshant48@myhunter.cuny.edu
#date: 16 sep,2019
#Image Blues
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('csBridge.png')   #Read in image from csBridge.png
#plt.imshow(img)		           #Load image into pyplot
#plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0
img2[:,:,0] = 0          #Set the red channel to 0

#plt.imshow(img2)         #Load our new image into pyplot
#plt.show()               #Show the image (waits until closed to continue)

plt.imsave('blueH.png', img2)
