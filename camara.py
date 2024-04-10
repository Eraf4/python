import cv2

capture = cv2.VideoCapture("rtsp://:8554/micamara")

while (capture.isOpened()):
    rest, frame = capture.read()
    cv2.imshow('Webcan',frame)
    if (cv2.waitKey(1) == ord('s')):
        break
capture.release()
cv2.destroyAllWindows()