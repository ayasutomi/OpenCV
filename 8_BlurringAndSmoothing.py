import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsd = hue sat value
    lower_red = np.array([133,0,0])
    upper_red = np.array([200,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/255
    smoothed =cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15,15),0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15,75,75)


    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()