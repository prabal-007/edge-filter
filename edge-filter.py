import cv2 as cv
import numpy as np
import time


def canny():
    while True:
        check, frame = camera.read()

        edges = cv.Canny(frame, 200, 150)
        cv.imshow('vid', edges)

        key = cv.waitKey(1)
        if key == ord('q'):
            break
    camera.release()
    cv.destroyAllWindows()


def sobel():
    while True:
        check, frame = camera.read()
        sobelx = cv.Sobel(camera, cv.CV_64F, 1, 0, ksize=31)
        ret, thresh = cv.threshold(sobelx, 0, 255.0, cv.THRESH_TOZERO)
        sobelx8 = np.uint8(sobelx)
        cv.imshow('sobel', sobelx8)

        key = cv.waitKey(1)
        if key == ord('q'):
            break
    camera.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    camera = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        option = input("press 1 for Canny or 2 for Sobel image : ")
        if option == "1":
            canny()
            break
        elif option == "2":
            sobel()
            break
        else:
            print("Invalid option")
            continue



