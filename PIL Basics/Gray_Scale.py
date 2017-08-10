#Created By: BWizz
#Date: 8/9/2017
#Experimentation with Python Image Lib 
from PIL import Image
import numpy as np
def sat(x,min,max):
	if x < min:
		x = min
	elif x > max:
		x = max
	else:
		x = x

	return x;


# Gray Scale Function with Contrast Adjustment
def greyScale(r,g,b,C):
	#Create Arrays from r,g,b image class
	rArray = np.array(r)
	gArray = np.array(g)
	bArray = np.array(b)
	#Determine image size
	w, h = rArray.shape
	#Initalize grayValue output array
	grayValue = np.zeros((w,h,1), dtype=np.uint8)

	#Determine constrast Multiplier
	# C can range from -255 to +255.
	# if C > 0, image will have more constrast.
	# if C < 0, image will be more dull.
	F = (259*(C+255))/(255*(259-C))

	for ii in range(0,w):
		for jj in range(0,h):
			#Determine corrected pixel
			r_Adj = F*(rArray[ii][jj] - 128) + 128
			g_Adj = F*(gArray[ii][jj] - 128) + 128
			b_Adj = F*(bArray[ii][jj] - 128) + 128
			#Calculate wieghted gray scale value
			grayValue[ii][jj] = sat(r_Adj*0.3 + g_Adj*0.59 + b_Adj *.11,0,255)
	return grayValue

myPic = Image.open("Ellie.jpg")
myPic.convert('RGB')
r,g,b = myPic.split()

#Create Grey Scale Image without any Contrast Correction
grayArray = greyScale(r,g,b,0)
grayImageArr = np.dstack([grayArray,grayArray,grayArray])
grayImage = Image.fromarray(grayImageArr,'RGB')
grayImage.save("Ellie_Gray.jpg")

#Create Grey Scale Image with Contrast Correction
grayAdjArray = greyScale(r,g,b,128);
grayImageAdjArr = np.dstack([grayAdjArray,grayAdjArray,grayAdjArray])
grayImageAdj = Image.fromarray(grayImageAdjArr,'RGB')
grayImageAdj.save("Ellie_Gray_Contrast_Adj.jpg")