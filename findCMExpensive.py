############################################################################################################
    # Team Id : PB#4097
    # Author List : Aditya Agrawal
    # Filename: findCM.py
    # Theme: Planterbot
    # Functions: GetColor(), GetShape()
    # Global Variables: Filename, file_names, shapes, colors, csvlist
#############################################################################################################

import cv2 #For OpenCV operations
import numpy as np #For numpy operations

def getColor(frame): #Main function
#############################################################################################
# Function Name: <Function Name>
# Input: < Inputs (or Parameters) list with description if any>
# Output: < Return value with description if any>
# Logic: <Description of the function performed and the logic used
# in the function>
# Example Call: <Example of how to call this function>
#############################################################################################
    #cv2.imshow('findCM Frame',frame)
    #cv2.waitKey(0)
    #global shape,color,number_of_shapes
    print 'inside getCM'
    shape='undefined'
    color='Undefined'
    number_of_shapes=0


    blue_down = np.array([100, 90, 90])
    blue_up = np.array([150, 255, 255])
    green_down = np.array([50, 90, 80])
    green_up = np.array([70, 255, 255])
    blue_down_broad = np.array([100, 90, 90])
    blue_up_broad = np.array([150, 255, 255])
    green_down_broad = np.array([40, 90, 80])
    green_up_broad = np.array([80, 255, 255])
    #black_down=np.array([0, 0, 0])
    #black_up=np.array([180, 255, 50])
    #new_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #black_mask=cv2.inRange(new_frame, black_down, black_up)
    #black_mask=cv2.cvtColor(black_mask,cv2.COLOR_HSV2GRAY)
    #print type(black_mask)
    #print black_mask[1,1]
    #a,b,c = cv2.split(black_mask)
    #new_frame=new_frame-v
    #kernel = np.ones((5,5),np.uint8)
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #ret,thresh=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
    #cv2.imshow('thresh',thresh)
    #cv2.waitKey(0)
    #ret,thresholded_frame=cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
    
    #final_gray = cv2.inRange(gray, 30, 150)
    #cv2.imshow('findCM final_gray',final_gray)
    #cv2.waitKey(0)
    #opening = cv2.morphologyEx(final_gray, cv2.MORPH_OPEN, kernel)
    #im2, contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #framenew=frame.copy()
    #cv2.drawContours(framenew, contours, -1, (0,255,0), 3)
    #cv2.imshow('findCM contours',framenew)
    #cv2.waitKey(0)

    #cv2.imshow('gray',gray)
    #cv2.waitKey(0)
    #cv2.imshow('final_gray',final_gray)
    #cv2.waitKey(0)
    #cv2.imshow('opening',opening)
    #cv2.waitKey(0)
    #cv2.imshow('final_thresh',final_thresh)
    #cv2.waitKey(0)
    #if not contours:
     #       return 'None','None',0
    #else:
        #cnt = contours[0]
        #number_of_shapes=len(contours)
        #x,y,w,h = cv2.boundingRect(cnt)
        #final_frame= frame[y:y + h, x:x + w, :].copy()
        #converted=cv2.cvtColor(final_frame,cv2.COLOR_BGR2HSV)
    converted=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    print 'frame converted'
    #converted = cv2.cvtColor(final_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(converted, blue_down, blue_up)
    print 'masking done'
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        pass
    else:
        #cv2.imshow('blue mask',mask)
        #cv2.waitKey(0)
        #framenew=frame.copy()
        #cv2.drawContours(framenew, contours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        #global color
        print 'some blue contours detected'
        color='Blue'
        cnt = contours[0]
        #temp= contours[0]
        finalcontours=[]
        for cnt in (temp for temp in contours if (cv2.contourArea(temp)>400)):# and cv2.contourArea(temp)<3500)):
            #global number_of_shapes
            #print cv2.contourArea(cnt)
            number_of_shapes+=1
            finalcontours.append(cnt)

        #    if cv2.contourArea(cnt) > 300 and cv2.contourArea(cnt)<500: #SET VALUES V V V V V V IMP
        #framenew=frame.copy()
        #cv2.drawContours(framenew, finalcontours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        x,y,w,h = cv2.boundingRect(cnt)
        newframe=converted[y-20:y+h+20,x-20:x+w+20,:]
        #cv2.imshow('some frame',newframe)
        #cv2.waitKey(0)

        mask = cv2.inRange(newframe, blue_down_broad, blue_up_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(framenew, contoursnew, -1, (0,255,0), 3)
        #cv2.imshow('frame new',newframe)
        #cv2.waitKey(0)
        #print len(contoursnew)

        if not contoursnew:
            pass
        else:
            cont=contoursnew[0]
            for cont in contoursnew:
                if cv2.contourArea(cont)>400:# and cv2.contourArea(cont)<3500:
                    #global shape
                    shape=getShape(cont)
                    break
            #break
            #number_of_shapes=len(contours)
            #shape=getShape(contours[0])
            if number_of_shapes>0:
            	#global shape,color,number_of_shapes
                return shape,color,number_of_shapes
            else:
                pass



    mask = cv2.inRange(converted, green_down, green_up)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        pass
    else:
        print 'some green contours detected'
        #cv2.imshow('green mask',mask)
        #cv2.waitKey(0)
        #framenew=frame.copy()
        #cv2.drawContours(framenew, contours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        #global color
        color= 'Green'
        cnt = contours[0]
        #temp= contours[0]
        finalcontours=[]
        for cnt in (temp for temp in contours if (cv2.contourArea(temp)>400)):# and cv2.contourArea(temp)<5000)):
            #global number_of_shapes
            #print 'incrementing green'
            number_of_shapes+=1
            finalcontours.append(cnt)
        #    if cv2.contourArea(cnt) > 300 and cv2.contourArea(cnt)<500: #SET VALUES V V V V V V IMP
        #framenew=frame.copy()
        #cv2.drawContours(framenew, finalcontours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        x,y,w,h = cv2.boundingRect(cnt)
        newframe=converted[y-20:y+h+20,x-20:x+w+20]
        mask = cv2.inRange(newframe, green_down_broad, green_up_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if not contoursnew:
            pass
        else:

            cont=contoursnew[0]
            for cont in contoursnew:
                if cv2.contourArea(cont)>400:# and cv2.contourArea(cont)<2500:
                    #global shape
                    shape=getShape(cont)
                    break
            #break
            #number_of_shapes=len(contours)
            #shape=getShape(contours[0])
            if number_of_shapes>0:
            	#global shape,color,number_of_shapes
                return shape,color,number_of_shapes
            else:
                pass




    lower_red = np.array([0, 90, 50])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(converted, lower_red, upper_red)
    lower_red = np.array([170, 90, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(converted, lower_red, upper_red)
    mask = mask0 + mask1
    lower_red_one_broad = np.array([0, 90, 50])
    upper_red_one_broad = np.array([20, 255, 255])
    #mask0 = cv2.inRange(converted, lower_red, upper_red)
    lower_red_two_broad = np.array([160, 90, 50])
    upper_red_two_broad = np.array([180, 255, 255])
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       
    if not contours:
        pass
    else:
        print 'some red contours detected'
        #cv2.imshow('red mask',mask)
        #cv2.waitKey(0)
        #framenew=frame.copy()
        #cv2.drawContours(framenew, contours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        #global color
        color= 'Red'
        cnt = contours[0]
        temp= contours[0]
        finalcontours=[]
        for cnt in (temp for temp in contours if (cv2.contourArea(temp)>400)):# and cv2.contourArea(temp)<2500)):
            #global number_of_shapes
            number_of_shapes+=1
            finalcontours.append(cnt)

        #    if cv2.contourArea(cnt) > 300 and cv2.contourArea(cnt)<500: #SET VALUES V V V V V V IMP
        #framenew=frame.copy()
        #cv2.drawContours(framenew, finalcontours, -1, (0,255,0), 3)
        #cv2.imshow('frame new',framenew)
        #cv2.waitKey(0)
        x,y,w,h = cv2.boundingRect(cnt)
        newframe=converted[y-20:y+h+20,x-20:x+w+20]
        mask = cv2.inRange(newframe, lower_red_one_broad, upper_red_one_broad)+cv2.inRange(newframe, lower_red_two_broad, upper_red_two_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if not contoursnew:
            pass
        else:
            cont=contoursnew[0]
            for cont in contoursnew:
                if cv2.contourArea(cont)>400:# and cv2.contourArea(cont)<1500:
                    #global shape
                    shape=getShape(cont)
                    break
            #break
            #number_of_shapes=len(contours)
            #shape=getShape(contours[0])
            if number_of_shapes>0:
            	#global shape,color,number_of_shapes
                return shape,color,number_of_shapes
            else:
                pass


    return shape,color,number_of_shapes

def getShape(cnt):
#############################################################################################
# Function Name: <Function Name>
# Input: < Inputs (or Parameters) list with description if any>
# Output: < Return value with description if any>
# Logic: <Description of the function performed and the logic used
# in the function>
# Example Call: <Example of how to call this function>
#############################################################################################
    #M = cv2.moments(cnt)
    #    #print M
    #if M['m00']==0:
    #    cx=0
     #   cy=0
    #else:
    #    cx = int(M['m10'] / M['m00'])
    #    cy = int(M['m01'] / M['m00'])

    shape = "Undefined"
    peri = 0.05 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, peri, True)
    if len(approx) == 3:
        shape = 'Triangle'

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
    elif len(approx) == 4:
        shape='Square'
    else:
        shape='Circle'
    return shape
####################################################################################
#TO DO: IMPLEMENT TEMPLATE MATCHING OR HAAR CASCADES (UPDATE: NO USE)
if __name__=='__main__':
    frame=cv2.imread('image2.jpg')
    shape,color,number_of_shapes=getColor(frame)
    print shape,color,str(number_of_shapes)
