import cv2 as cv
import numpy as np

def canny(image):
    edges = cv.Canny(image, 200, 40)
    cv.imshow('mes1', edges)
    cv.waitKey(0)

def sobel(img):
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=31)
    # ret, thresh = cv.threshold(sobelx, 0, 255.0, cv.THRESH_TOZERO)
    sobelx8 = np.uint8(sobelx)
    cv.imshow('sobel', sobelx8)
    cv.waitKey(0)

if __name__ == '__main__':
    img = cv.imread('***************\\messi.jpg', 0)                 # ** = path of the picture
    img = cv.resize(img, (800, 600))
    while True:
        option = input("press 1 for Canny or 2 for Sobel image : ")
        if option == "1":
            canny(img)
            break
        elif option == "2":
            sobel(img)
            break
        else:
            print("Invalid option")
            continue
