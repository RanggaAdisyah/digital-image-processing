import cv2

img = cv2.imread(r'Foto\gambar.jpeg')

cv2.imshow('Citra Asli', img)
print('Nilai Citra Asli', img)

reflection = cv2.flip(img, 0)

print('Nilai Citra Setelah Refleksi', reflection)
cv2.imshow('Hasil Refleksi', reflection)
cv2.waitKey()