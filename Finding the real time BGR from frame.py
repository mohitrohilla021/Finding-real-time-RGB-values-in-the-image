# there are many mouse events available in cv2 package

import cv2
import numpy as np

# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img1[y,x,0]      # index is 0
        green = img1[y, x, 1]   # index is 1
        red = img1[y, x, 2]     # index is 2
        font=cv2.FONT_HERSHEY_SIMPLEX
        strBGR= str(blue)+', '+str(green)+', '+str(red)
        cv2.putText(img1,strBGR,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow('image',img1)

img1=cv2.imread('one.jpg')
cv2.imshow('image',img1)
cv2.setMouseCallback('image',click_event)

cv2.waitKey()
cv2.destroyAllWindows()
