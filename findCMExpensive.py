import cv2
import numpy as np

def getColor(frame):
    shape = 'Undefined'
    color = 'Undefined'
    number_of_shapes = 0
    
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    blue_down = np.array([100, 90, 90])
    blue_up = np.array([150, 255, 255])
    green_down = np.array([50, 100, 100])
    green_up = np.array([70, 255, 255])
    blue_down_broad = np.array([100, 90, 90])
    blue_up_broad = np.array([150, 255, 255])
    green_down_broad = np.array([40, 90, 90])
    green_up_broad = np.array([80, 255, 255])
    
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(converted, blue_down, blue_up)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        pass
    else:
        color = 'Blue'
        cnt = contours[0]
        finalcontours = []
        
        for cnt in (temp for temp in contours if (cv2.contourArea(temp) > 300 and cv2.contourArea(temp) < 500)):
            number_of_shapes += 1
            finalcontours.append(cnt)
            
        x, y, w, h = cv2.boundingRect(cnt)
        newframe = converted[y - 20:y + h + 20, x - 20:x + w + 20]
        mask = cv2.inRange(newframe, green_down_broad, green_up_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = contoursnew[0]
        
        for cont in contoursnew:
            if cv2.contourArea(cont) > 300 and cv2.contourArea(cont) < 500:
                shape = getShape(cont)
                break
        
        if number_of_shapes > 0:
            return shape, color, number_of_shapes
        else:
            pass
    
    mask = cv2.inRange(converted, green_down, green_up)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        pass
    else:
        color = 'Green'
        cnt = contours[0]
        finalcontours = []
        
        for cnt in (temp for temp in contours if (cv2.contourArea(temp) > 300 and cv2.contourArea(temp) < 500)):
            number_of_shapes += 1
            finalcontours.append(cnt)
            
        x, y, w, h = cv2.boundingRect(cnt)
        newframe = converted[y - 20:y + h + 20, x - 20:x + w + 20]
        mask = cv2.inRange(newframe, green_down_broad, green_up_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = contoursnew[0]
        
        for cont in contoursnew:
            if cv2.contourArea(cont) > 300 and cv2.contourArea(cont) < 500:
                shape = getShape(cont)
                break
        
        if number_of_shapes > 0:
            return shape, color, number_of_shapes
        else:
            pass
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(converted, lower_red, upper_red)
    lower_red = np.array([170, 100, 100])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(converted, lower_red, upper_red)
    mask = mask0 + mask1
    lower_red_one_broad = np.array([0, 90, 90])
    upper_red_one_broad = np.array([20, 255, 255])
    lower_red_two_broad = np.array([160, 90, 90])
    upper_red_two_broad = np.array([180, 255, 255])
    
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        pass
    else:
        color = 'Red'
        cnt = contours[0]
        finalcontours = []
        
        for cnt in (temp for temp in contours if (cv2.contourArea(temp) > 300 and cv2.contourArea(temp) < 500)):
            number_of_shapes += 1
            finalcontours.append(cnt)
        
        x, y, w, h = cv2.boundingRect(cnt)
        newframe = converted[y - 20:y + h + 20, x - 20:x + w + 20]
        mask = cv2.inRange(newframe, lower_red_one_broad, upper_red_one_broad) + cv2.inRange(newframe, lower_red_two_broad, upper_red_two_broad)
        im2, contoursnew, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = contoursnew[0]
        
        for cont in contoursnew:
            if cv2.contourArea(cont) > 300 and cv2.contourArea(cont) < 500:
                shape = getShape(cont)
                break
        
        if number_of_shapes > 0:
            return shape, color, number_of_shapes
        else:
            pass
    
    return shape, color, number_of_shapes

def getShape(cnt):
    M = cv2.moments(cnt)
    
    if M['m00'] == 0:
        cx = 0
        cy = 0
    else:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
    shape = "Undefined"
    peri = 0.03 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, peri, True)
    
    if len(approx) == 3:
        shape = 'Triangle'
    elif len(approx) == 4:
        shape = 'Square'
    else:
        shape = 'Circle'
    
    return shape
