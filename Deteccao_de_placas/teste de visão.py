from turtle import shapetransform
import cv2
import numpy as np

#Exemplos de manipulação de imagens , filtros e peças

img = cv2.imread('C:/Users/maxna/Desktop/pixel_art.jpg', cv2.IMREAD_COLOR) 
cv2.namedWindow('janela_01')
cv2.imshow('janela_01', img)
cv2.waitKey()

# filtro 1

filtro = np.ones(img.shape, dtype=np.uint8) * 110
somada = cv2.add(img, filtro)
cv2.namedWindow('janela_02')
cv2.imshow('janela_02', somada)

cv2.waitKey()

#filtro 2
subtraida = cv2.subtract(img, filtro)
cv2.namedWindow('janela_03')
cv2.imshow('janela_03', subtraida)

cv2.waitKey()

#kernel

kernel_blur = np.ones((9,9), np.float32)/81

blurred = cv2.filter2D(img,-1, kernel_blur)

cv2.namedWindow('janela_blur')
cv2.imshow('janela_blur', blurred)
cv2.waitKey()

#gaussian_blurred

gaussian_blurred = cv2.GaussianBlur(img,(5,5), 0)
cv2.namedWindow("janela_gaussian")
cv2.imshow("janela_gaussian", gaussian_blurred)
cv2.waitKey()

#sharpening

sharped_blurr = np.array([[-1,-1,-1],
                         [-1,9,-1],
                         [-1,-1,-1]])
sharpened = cv2.filter2D(gaussian_blurred,-1,sharped_blurr)
cv2.namedWindow('sharpened')
cv2.imshow('sharpened', sharpened)
cv2.waitKey()

#Canny Edges
edges = cv2.Canny(gaussian_blurred, 50, 240)
cv2.namedWindow('Edges - Detecção de bordas')
cv2.imshow('Edges - Detecção de bordas', edges)
cv2.waitKey()

edges = cv2.Canny(img, 50, 240)
cv2.namedWindow('Edges 02 - Detecção de bordas')
cv2.imshow('Edges 02 - Detecção de bordas', edges)
cv2.waitKey()

#Laplacian

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.namedWindow('Laplaciano - Detecção de bordas')
cv2.imshow('Laplaciano - Detecção de bordas', edges)
cv2.waitKey()