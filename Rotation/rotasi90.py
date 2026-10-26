import cv2

img = cv2.imread(r'Foto\gambar.jpeg')

cv2.imshow('Citra Asli', img)
print('Nilai Citra Asli', img)

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 90, 1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))

print('Nilai Citra Setelah Rotasi', img_rotation)
cv2.imshow('Hasil Rotasi', img_rotation)
cv2.waitKey()