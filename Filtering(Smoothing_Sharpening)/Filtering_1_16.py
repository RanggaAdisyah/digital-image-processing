import cv2
import numpy as np
from matplotlib import pyplot as plt

# Daftar jalur gambar
image_paths = [r'Foto\1.jpg', 
               r'Foto\2.jpg', 
               r'Foto\3.jpg']

# Kernel smoothing (mean filter) dengan nilai 1/16
mean = np.array([[0.0625, 0.125, 0.0625], 
                 [0.125, 0.25, 0.125], 
                 [0.0625, 0.125, 0.0625]])


# Siapkan canvas untuk 3 gambar dengan 2 kolom (gambar asli dan hasil filter)
fig, axs = plt.subplots(len(image_paths), 2, figsize=(10, 12))

for i, path in enumerate(image_paths):
    # Baca gambar
    I = cv2.imread(path)
    img = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

    # Terapkan smoothing
    im = cv2.filter2D(img, -1, mean)

    # Tampilkan gambar asli
    axs[i, 0].imshow(img, cmap='gray')
    axs[i, 0].set_title(f'Original Image {i+1}', fontsize=10, color='white')
    axs[i, 0].axis('off')

    # Tampilkan hasil smoothing
    axs[i, 1].imshow(im, cmap='gray')
    axs[i, 1].set_title(f'Smoothed Image {i+1}', fontsize=10, color='white')
    axs[i, 1].axis('off')

# Sesuaikan tata letak agar tidak saling tumpang tindih
plt.tight_layout()
plt.show()
