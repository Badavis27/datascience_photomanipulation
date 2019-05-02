
#https://stackoverflow.com/questions/24089924/skip-over-a-value-in-the-range-function-in-python




from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image
#import Image

#use input() python 3, raw_input python 2x
user = int(raw_input ("Enter your change threshold: "))



img_list=[]
for i in range (4) + range (5, 7) + range (8, 12) + range (13, 73) + range (74, 130) + range (132, 134) + range (135, 142) + range (143, 147) + range (149, 200):
	filename = "rebelmrkt_" + str(i) + ".jpg"
	img = Image.open(filename)
	img = np.float32(img)
	#img = np.clip(img,0,255)
	#img = np.uint8(img)
	img_list.append(img)




# getting average image
avg_img = []

for img in img_list:
	try:
		avg_img = avg_img +img
	except:
		avg_img = img

avg_img /= len(img_list)
#avg_img = np.float32(avg_img)
#avg_img_t = np.clip(avg_img, 0, 255)
#avg_img_t = np.uint8(avg_img_t)


#variance
img_list2=[]
for i in range (4) + range (5, 7) + range (8, 12) + range (13, 73) + range (74, 130) + range (132, 134) + range (135, 142) + range (143, 147) + range (149, 200):
	filename2 = "rebelmrkt_" + str(i) + ".jpg"
	img2 = Image.open(filename2)
	img2 = np.float32(img2)
	img2 = (img2 - avg_img)**2
	img_list2.append(img2)

var_img = []

for img2 in img_list2:
	try:
		var_img = var_img + img2
	except:
		var_img = img2


var_img /= len(img_list2)

#Standard Deviaion
SD_img = (var_img)**(1/2)
'''SD_img = np.clip(SD_img, 0, 255)
SD_img = np.uint8(SD_img)'''



if user >= 0 and user <= 255:
	for row in range(len(SD_img)):
		for col in range(len(SD_img[row])):
			if SD_img[row][col][0] > user or SD_img[row][col][1] > user or SD_img[row][col][2] > user:
			#if(SD_img[row][col] > user).any():
				avg_img[row][col] = [255,0,0]
				#break
else: 
	print "enter in a threshhold between 0 and 255"

SD_img = np.clip(SD_img, 0, 255)
SD_img = np.uint8(SD_img)

avg_img = np.clip(avg_img, 0, 255)
avg_img = np.uint8(avg_img)


mplot.imshow(avg_img)
mplot.show()

