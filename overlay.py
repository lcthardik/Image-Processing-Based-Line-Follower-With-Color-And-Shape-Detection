import cv2
import imutils as im
import numpy as np
import csvreader as csv
plantation=cv2.imread('Plantation.png')
zonenumber=0
#zones={'zone11':(310,290),'zone12':(350,290),'zone13':(390,290),'zone14':(430,290),'zone21':(120,220),'zone22':(150,220),'zone23':(70,250),'zone24':(130,250),'zone31':(230,200),'zone32':(270,200),'zone33':(310,200),'zone34':(350,200),'zone41':(510,205),'zone42':(540,205),'zone43':(570,205),'zone44':(600,205)}
zones={'zone11':(350,290),'zone12':(420,290),'zone13':(490,290),'zone14':(560,290),'zone21':(110,220),'zone22':(160,220),'zone23':(70,250),'zone24':(125,250),'zone31':(230,210),'zone32':(285,210),'zone33':(280,174),'zone34':(320,174),'zone41':(462,200),'zone42':(509,200),'zone43':(557,200),'zone44':(604,200)}
files={}
def updateZone():
	global zonenumber
	zonenumber=zonenumber+1
def setFiles(filenames):
	global files
	files=filenames
	showPlantation()
def overlay(color,shape,number):
	print color,shape,number
	updateZone()
	global files,zonenumber,plantation
	key=color+shape
	filename=files[key]
	#print filename
	file_path='Images/'+filename
	overlayimg=cv2.imread(file_path,-1)
	#cv2.imshow('ol',overlayimg)
	#cv2.waitKey(0)
	#resized_image= im.resize(overlayimg,width=26)
	basic_string='zone'+str(zonenumber)
	cols=0
	if basic_string=='zone1' or basic_string=='zone2':
		resized_image= im.resize(overlayimg,width=50)
		cols=50
	elif basic_string=='zone3':
		resized_image= im.resize(overlayimg,width=40)
		cols=40
	else:
		resized_image= im.resize(overlayimg,width=45)
		cols=45
	rows=resized_image.shape[0]
	
	for i in range(number):
		string=basic_string+str(i+1)
		xcoord=zones[string][0]
		ycoord=zones[string][1]
		print rows
		print type(rows)
		#cv2.imshow('plantation',plantation)
		#cv2.waitKey(0)
		#cv2.imshow('overlayimg',resized_image)
		#cv2.waitKey(0)
		
		#cv2.imshow('plantation',passed_frame)
		#cv2.waitKey(0)
		plantation[(ycoord-rows):ycoord,xcoord:(xcoord+cols)]=addWeighted(plantation[(ycoord-rows):ycoord,xcoord:(xcoord+cols)],resized_image)
def showPlantation():
	global plantation
	cv2.imshow('plantation',plantation)
	

def addWeighted(face_image,overlay_image):
	# Split out the transparency mask from the colour info
    overlay_img = overlay_image[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_image[:,:,3:]  # And the alpha plane
    #print 'Overlay shape'
    #print overlay_t_img.shape
    #print 'face image shape'
    #print face_img.shapere
    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask
    #cv2.imshow('face',face_image)
    #cv2.waitKey(0)
    #cv2.imshow('ol',overlay_mask)
    #cv2.waitKey(0)
			

    #print 'bg mask shape'
    #print background_mask.shape
    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_image * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))

if __name__=='__main__':
	csv.CSVInitialize()
	setFiles(csv.CSVRead())
	overlay('Red','Circle',4)
	overlay('Blue','Square',4)
	overlay('Red','Square',4)
	overlay('Red','Square',4)
	showPlantation()
	cv2.waitKey(0)
	cv2.destroyAllWindows()