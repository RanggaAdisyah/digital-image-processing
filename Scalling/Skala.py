import cv2

img = cv2.imread(r'Foto\gambar.jpeg')

cv2.imshow('Citra Asli', img)
print('Nilai Citra Asli', img)

num_rows, num_cols = img.shape[:2]
new_rows, new_cols = int(num_rows*2), int(num_cols*0.5)
img_scaled = cv2.resize(img, (new_rows, new_cols))

cv2.imshow('Hasil Skala', img_scaled)
print('Nilai Citra Setelah Skala', img_scaled)
cv2.waitKey()