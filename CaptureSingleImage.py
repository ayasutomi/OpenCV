from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    # namedWindow("cam-test",CV_)
    imshow("cam-test",img)
    waitKey(0)
    destroyAllWindows()
    imwrite("watch.jpg",img) #save image