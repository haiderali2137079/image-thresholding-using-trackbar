import cv2
img=cv2.imread("haider.jpg",0)
img=cv2.resize(img,(600,600))
cv2.namedWindow("wn")
def cross(x):
    pass
cv2.createTrackbar("thold value","wn",0,255,cross)
while True:
    x=cv2.getTrackbarPos("thold value","wn")
    _,th=cv2.threshold(img,x,255,cv2.THRESH_BINARY)
    cv2.imshow("wn",th)
    if cv2.waitKey(1) &0xff==27:
        break
cv2.destroyAllWindows()
