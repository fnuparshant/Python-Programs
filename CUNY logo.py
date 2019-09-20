#name: Fnu Parshant
#Email: fnu.parshant48@myhunter.cuny.edu
#date: 18 sep,2019
#CUNY LOGO
import matplotlib.pyplot as plt
import numpy as np

logoImg = np.ones((30,30,3))

logoImg[0:30,0:10,0:2]=0
logoImg[20:30,0:30,0:2]=0
logoImg[0:10,0:30,0:2]=0

plt.imsave("logo.png", logoImg)
plt.imshow(logoImg)
plt.show() 
