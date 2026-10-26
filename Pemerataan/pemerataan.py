import cv2
import numpy as np
from matplotlib import pyplot as plt

def perataanHistogram(A):
    nilai_bin = 256
    A = A + 1
    [frekuensi, value] = np.histogram(A, bins=nilai_bin)
    cumulatif_histogram = frekuensi.cumsum()
    [baris, kolom] = A.shape
    probabilty_frekuensi = np.round((cumulatif_histogram / float(A.size)) * (nilai_bin - 1))
    B = np.empty(A.shape)
    for i in range(baris):
        for j in range(kolom):
            B[i, j] = probabilty_frekuensi[int(A[i, j]) - 1]
    return B

# Membaca ketiga gambar
I1 = cv2.imread(r'Pemerataan\1.jpg')
I2 = cv2.imread(r'Pemerataan\2.jpg')
I3 = cv2.imread(r'Pemerataan\3.jpg')

# Mengubah gambar ke grayscale
gray1 = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(I2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(I3, cv2.COLOR_BGR2GRAY)

# Melakukan perataan histogram pada masing-masing gambar
hasil1 = perataanHistogram(gray1)
hasil2 = perataanHistogram(gray2)
hasil3 = perataanHistogram(gray3)

# Membuat frame pertama untuk gambar asli dan hasil perataan histogram
fig1, axs1 = plt.subplots(3, 2, figsize=(10, 10))
fig1.suptitle('Perataan Histogram untuk Tiga Gambar dengan Kontras Berbeda')

# Menampilkan gambar grayscale dan hasil perataan histogram untuk gambar pertama
axs1[0, 0].imshow(gray1, cmap='gray')
axs1[0, 0].set_title('Gambar Asli - Kontras Tinggi')
axs1[0, 0].axis('off')

axs1[0, 1].imshow(hasil1, cmap='gray')
axs1[0, 1].set_title('Hasil Perataan - Kontras Tinggi')
axs1[0, 1].axis('off')

# Menampilkan gambar grayscale dan hasil perataan histogram untuk gambar kedua
axs1[1, 0].imshow(gray2, cmap='gray')
axs1[1, 0].set_title('Gambar Asli - Kontras Sedang')
axs1[1, 0].axis('off')

axs1[1, 1].imshow(hasil2, cmap='gray')
axs1[1, 1].set_title('Hasil Perataan - Kontras Sedang')
axs1[1, 1].axis('off')

# Menampilkan gambar grayscale dan hasil perataan histogram untuk gambar ketiga
axs1[2, 0].imshow(gray3, cmap='gray')
axs1[2, 0].set_title('Gambar Asli - Kontras Rendah')
axs1[2, 0].axis('off')

axs1[2, 1].imshow(hasil3, cmap='gray')
axs1[2, 1].set_title('Hasil Perataan - Kontras Rendah')
axs1[2, 1].axis('off')

# Frame kedua untuk menampilkan histogram dari hasil perataan histogram
fig2, axs2 = plt.subplots(1, 3, figsize=(15, 5))
fig2.suptitle('Histogram dari Hasil Perataan Histogram')

# Menampilkan histogram untuk setiap hasil perataan
axs2[0].hist(hasil1.ravel(), 256, [0, 256])
axs2[0].set_title('Histogram - Kontras Tinggi')
axs2[0].set_xlim([0, 256])

axs2[1].hist(hasil2.ravel(), 256, [0, 256])
axs2[1].set_title('Histogram - Kontras Sedang')
axs2[1].set_xlim([0, 256])

axs2[2].hist(hasil3.ravel(), 256, [0, 256])
axs2[2].set_title('Histogram - Kontras Rendah')
axs2[2].set_xlim([0, 256])

# Menampilkan hasil
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()

# Menampilkan gambar di window menggunakan OpenCV
# cv2.imshow('Gray - Kontras Tinggi', gray1)
# cv2.imshow('Perataan - Kontras Tinggi', hasil1)
# cv2.imshow('Gray - Kontras Sedang', gray2)
# cv2.imshow('Perataan - Kontras Sedang', hasil2)
# cv2.imshow('Gray - Kontras Rendah', gray3)
# cv2.imshow('Perataan - Kontras Rendah', hasil3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()