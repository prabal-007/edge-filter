import cv2 as cv
import numpy as np

def canny(image):
    edges = cv.Canny(image, 200, 40)
    cv.imshow('mes1', edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

def sobel(img):
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=31)
    # ret, thresh = cv.threshold(sobelx, 0, 255.0, cv.THRESH_TOZERO)
    sobelx8 = np.uint8(sobelx)
    cv.imshow('sobel', sobelx8)
    cv.waitKey(0)
    cv.destroyAllWindows()

def comp(img):
    edges = cv.Canny(img, 200, 40)
    cv.imshow('mes1', img)
    cv.waitKey(0)
    cv.imshow('mes', edges)
    cv.waitKey(0)
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=31)
    sobelx8 = np.uint8(sobelx)
    cv.imshow('sobel', sobelx8)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    img = cv.imread('C:\\Users\\admin\\Downloads\\messi.jpg', 0)
    img = cv.resize(img, (600, 600))
    while True:
        option = input("press 1 for Canny or 2 for Sobel 3 for original image and 4 for all : ")
        if option == "1":
            canny(img)
            continue
        elif option == "2":
            sobel(img)
            continue
        elif option == "3":
            cv.imshow('img2', img)
            cv.waitKey(0)
            cv.destroyAllWindows()
            continue
        elif option == "4":
            comp(img)
            continue
        elif option == "0":
            break
        else:
            print("Invalid option")
            continue
