## Workflow of the Threshold-Based Segmentation Script

### Prerequisites

* **Python 3.x**
* **OpenCV** and **Matplotlib** installed via:

  ```bash
  pip install opencv-python matplotlib
  ```
* Source images placed in a `Foto` directory, named `1.jpg` and `2.jpg` (or adjust paths as needed).

---

### Step-by-Step Guide

1. **Import Libraries**

   ```python
   import cv2
   import numpy as np
   from matplotlib import pyplot as plt
   ```

   * **cv2** for image I/O and thresholding
   * **numpy** for array operations (used implicitly)
   * **matplotlib.pyplot** for plotting images and histograms

2. **Define the Segmentation Function**

   ```python
   def segment_image_with_threshold(image_path, threshold_value):
       image = cv2.imread(image_path)
       if image is None:
           print(f"Gambar {image_path} tidak ditemukan.")
           return None

       if len(image.shape) == 3:
           image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

       _, binary_image = cv2.threshold(
           image,
           threshold_value,
           255,
           cv2.THRESH_BINARY
       )

       return image, binary_image
   ```

   * **Read** the image from `image_path`.
   * **Check** if the image was loaded; print a message if not.
   * **Convert** to grayscale if it has three channels.
   * **Apply** global thresholding at `threshold_value` to get a binary (black & white) image.
   * **Return** both the original grayscale and the binary images.

3. **Define the Display Function**

   ```python
   def display_images_with_histogram(
       original, segmented,
       title_original, title_segmented, title_histogram
   ):
       plt.figure(figsize=(15, 5))

       # Show original grayscale
       plt.subplot(1, 3, 1)
       plt.imshow(original, cmap='gray')
       plt.title(title_original)
       plt.axis('off')

       # Show segmented (binary)
       plt.subplot(1, 3, 2)
       plt.imshow(segmented, cmap='gray')
       plt.title(title_segmented)
       plt.axis('off')

       # Plot histogram of original
       plt.subplot(1, 3, 3)
       plt.hist(
           original.ravel(),
           bins=256,
           range=(0, 256),
           color='blue',
           alpha=0.7
       )
       plt.title(title_histogram)
       plt.xlabel('Intensitas Pixel')
       plt.ylabel('Frekuensi')
       plt.grid(axis='y', linestyle='--', alpha=0.7)

       plt.tight_layout()
       plt.show()
   ```

   * **Figure setup** with three panels: original image, segmented image, and histogram.
   * **Original panel**: shows grayscale image.
   * **Segmented panel**: shows the binary result.
   * **Histogram panel**: plots pixel‐intensity distribution of the original.

4. **Main Execution Loop**

   ```python
   if __name__ == "__main__":
       image_paths = [r"Foto\1.jpg", r"Foto\2.jpg"]
       threshold_value = 127  

       for i, image_path in enumerate(image_paths):
           original, segmented = segment_image_with_threshold(
               image_path,
               threshold_value
           )
           if original is not None:
               display_images_with_histogram(
                   original,
                   segmented,
                   f"Gambar Asli {i+1}",
                   f"Hasil Thresholding {i+1}",
                   f"Histogram Gambar Asli {i+1}"
               )
   ```

   * **List** of input image paths and a chosen **threshold value** (127).
   * **Loop** over each image:

     1. Call `segment_image_with_threshold`.
     2. If successful, call `display_images_with_histogram` to visualize results.
