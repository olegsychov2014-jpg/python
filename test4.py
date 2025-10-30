from cv2 import cv2
import requests

cam = cv2.videocapture(0)

while True:
    ret, img = cam.read()
    cv2.imshow("camera",img)
    if cv2.waitkey(10) == 27:
        break
cam.releases()
cv2.destroyAllwindows()

