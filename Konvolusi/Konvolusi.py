import cv2
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# Baca 3 gambar
image_paths = [r'Foto\1.jpg', 
               r'Foto\2.jpg', 
               r'Foto\3.jpg']

# Kernel filter
w_k = np.array([[0, 0, 0], 
                [0, 1, 0], 
                [0, 0, 0]], dtype='float')

w_k = np.rot90(w_k, 2)

# Plot hasil
fig, axs = plt.subplots(3, 2, figsize=(12, 12))  # Ukuran figure yang proporsional
for i, path in enumerate(image_paths):
    # Baca gambar dan konversi ke grayscale
    imgc = cv2.imread(path)
    img = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)

    # Filter dengan convolution
    f = signal.convolve2d(img, w_k, 'valid')

    # Tampilkan gambar original dan hasil filter
    axs[i, 0].imshow(img, cmap='gray')
    axs[i, 0].set_title(f'Original Image {i+1}', color='white', fontsize=12)
    axs[i, 0].axis('off')
    
    axs[i, 1].imshow(f, cmap='gray')
    axs[i, 1].set_title(f'Filtered Image {i+1}', color='white', fontsize=12)
    axs[i, 1].axis('off')

# Sesuaikan layout agar tidak terlalu mepet
plt.subplots_adjust(wspace=0.2, hspace=0.3)

# Warna latar belakang hitam untuk lebih kontras
fig.patch.set_facecolor('black')

# Tampilkan semua hasil
plt.tight_layout()
plt.show()
