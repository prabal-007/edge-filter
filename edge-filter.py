import cv2 as cv
import time

video = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    check, frame = video.read()
#     print(frame)

    edges = cv.Canny(frame, 200, 150)
    cv.imshow('vid', edges)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv.destroyAllWindows()
