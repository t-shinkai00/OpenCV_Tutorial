# http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html#hough-circles
import cv2
import numpy as np

img = cv2.imread('data/opencv-logo-white.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
input=cv2.waitKey(0)&0xFF
if input == ord('q'):         # wait for 'q' key to exit
    cv2.destroyAllWindows()
elif input == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('circles.png',cimg)
    cv2.destroyAllWindows()