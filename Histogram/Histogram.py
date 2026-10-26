import cv2
import numpy as np

from matplotlib import pyplot as plt  #untuk menampilkan grafik

img1 = cv2.imread(r'Histogram\1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'Histogram\2.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(r'Histogram\3.jpg', cv2.IMREAD_GRAYSCALE)



cv2.imshow('Grayscale1', img1)
plt.hist(img1.ravel(), 256, [0, 256]);
plt.show() #menggunakan fungsi ravel() untuk menampilkan hist & penentuan batas max nilai pixel

cv2.imshow('Grayscale2', img2)
plt.hist(img2.ravel(), 256, [0, 256]);
plt.show()

cv2.imshow('Grayscale3', img3)
plt.hist(img3.ravel(), 256, [0, 256]);
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()