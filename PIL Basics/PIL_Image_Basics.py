#Created By: BWizz
#Date: 8/8/2017
#Experimentation with Python Image Lib 
from PIL import Image
import numpy as np


# Import Picture of Ellie
myPic = Image.open("Ellie.jpg")
myPic.convert('RGB')
# Display Image
#myPic.show()

#Split Image into RGB images
r,g,b = myPic.split()

#Load R G B into arrays
rArray = np.array(r)
gArray = np.array(g)
bArray = np.array(b)
w, h = rArray.shape

#Create zero Array
Zer = np.zeros((w,h,1), dtype=np.uint8)

#Combined R,G, B arraus into an image class
redImageArr = np.dstack((rArray,Zer,Zer))
blueImageArr = np.dstack((Zer,Zer,bArray))
greenImageArr = np.dstack((Zer,gArray,Zer))

#Create images & save.
redImage = Image.fromarray(redImageArr,'RGB')
redImage.save("Ellie_Red.jpg")

blueImage = Image.fromarray(blueImageArr,'RGB')
blueImage.save("Ellie_Blue.jpg")

greenImage = Image.fromarray(greenImageArr,'RGB')
greenImage.save("Ellie_Green.jpg")




