import cv2
import numpy as np

# Membaca gambar
img = cv2.imread("Foto/gambar.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Gambar Asli")
print(img)

# Mendapatkan nilai minimum dan maksimum dari gambar
min_val = np.amin(img)
max_val = np.amax(img)

H, W = img.shape[:2]
array_kontras = np.zeros((H, W), np.uint8)

# Menyesuaikan kontras
for i in range(H):
    for j in range(W):
        pixel = img[i, j].astype(float)  # Ubah ke tipe float untuk mencegah overflow
        pixel = (pixel - min_val) * 255 / (max_val - min_val)
        array_kontras[i, j] = np.clip(pixel, 128, 255)  # Menjaga agar nilai tetap dalam rentang 0-255

print("Array Kontras")
print(array_kontras)

# Menampilkan hasil
cv2.imshow("Sebelum", img)
cv2.imshow("Sesudah", array_kontras)

cv2.waitKey(0)  # Tunggu hingga pengguna menekan tombol
cv2.destroyAllWindows()  # Menutup semua jendela OpenCV