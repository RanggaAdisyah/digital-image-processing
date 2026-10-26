import cv2
import numpy as np

img = cv2.imread(r'Foto\gambar.jpeg')

cv2.imshow('Citra Asli', img)
print('Nilai Sebelum Translasi', img)

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([ [1,0,70], [0,1,60] ])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))

print('Nilai Setelah Translasi', img_translation)
cv2.imshow('Translasi Gambar', img_translation)
cv2.waitKey()