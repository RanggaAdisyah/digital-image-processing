import cv2
import numpy as np
from matplotlib import pyplot as plt

def segment_image_with_threshold(image_path, threshold_value):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Gambar {image_path} tidak ditemukan.")
        return None

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    return image, binary_image

def display_images_with_histogram(original, segmented, title_original, title_segmented, title_histogram):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original, cmap='gray')
    plt.title(title_original)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(segmented, cmap='gray')
    plt.title(title_segmented)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.hist(original.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.title(title_histogram)
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_paths = [r"Foto\1.jpg", r"Foto\2.jpg"]
    threshold_value = 127  

    for i, image_path in enumerate(image_paths):
        original, segmented = segment_image_with_threshold(image_path, threshold_value)
        if original is not None:
            display_images_with_histogram(
                original, segmented,
                f"Gambar Asli {i+1}", f"Hasil Thresholding {i+1}", f"Histogram Gambar Asli {i+1}"
            )