import cv2
import imutils as im
import numpy as np

plantation = cv2.imread('Plantation.png')
zonenumber = 0
zones = {'zone11': (350, 290), 'zone12': (420, 290), 'zone13': (490, 290), 'zone14': (560, 290), 'zone21': (110, 220), 'zone22': (160, 220), 'zone23': (70, 250), 'zone24': (125, 250), 'zone31': (230, 210), 'zone32': (285, 210), 'zone33': (280, 174), 'zone34': (320, 174), 'zone41': (510, 205), 'zone42': (540, 205), 'zone43': (570, 205), 'zone44': (600, 205)}
files = {}
overlayimgs = {}

def updateZone():
    global zonenumber
    zonenumber = zonenumber + 1

def setFiles(filenames):
    global files
    files = filenames
    
    for key, val in files.items():
        filename = files[key]
        file_path = 'Images/' + filename
        overlayimgs[key] = cv2.imread(file_path, -1)

def overlay(color, shape, number):
    print color, shape, number
    updateZone()
    global files, zonenumber, plantation
    key = color + shape
    
    overlayimg = overlayimgs[key]
    
    basic_string = 'zone' + str(zonenumber)
    
    if basic_string == 'zone1' or basic_string == 'zone2':
        resized_image = im.resize(overlayimg, width=50)
    elif basic_string == 'zone3':
        resized_image = im.resize(overlayimg, width=40)
    else:
        resized_image = im.resize(overlayimg, width=26)
    
    rows = resized_image.shape[0]
    
    for i in range(number):
        string = basic_string + str(i + 1)
        xcoord = zones[string][0]
        ycoord = zones[string][1]
        
        plantation[(ycoord - rows):ycoord, xcoord:(xcoord + 26)] = addWeighted(plantation[(ycoord - rows):ycoord, xcoord:(xcoord + 26)], resized_image)

def showPlantation():
    global plantation
    cv2.imshow('plantation', plantation)

def addWeighted(face_image, overlay_image):
    overlay_img = overlay_image[:, :, :3]
    overlay_mask = overlay_image[:, :, 3:]
    background_mask = 255 - overlay_mask

    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    face_part = (face_image * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))
