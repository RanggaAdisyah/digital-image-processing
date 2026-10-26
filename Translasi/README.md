## Workflow of the Image Translation Script

### Prerequisites

* **Python 3.x**
* **OpenCV** installed via:

  ```bash
  pip install opencv-python
  ```
* An image file located at `Foto/gambar.jpeg` (or adjust the path as needed).

---

### Description

This script demonstrates how to **translate** (shift) an image using OpenCV’s affine transformation. The code shifts the image 70 pixels to the right and 60 pixels down.

---

### Step-by-Step Guide

1. **Import OpenCV and NumPy**

   ```python
   import cv2
   import numpy as np
   ```

   * `cv2`: OpenCV module for reading, displaying, and transforming images.
   * `numpy`: Used for constructing the translation matrix.

2. **Load the Source Image**

   ```python
   img = cv2.imread(r'Foto\gambar.jpeg')
   ```

   * Reads the image from disk into a NumPy array `img` of shape `(height, width, channels)` in BGR color order.
   * If the path is incorrect or the file is missing, `img` will be `None`.

3. **Display & Inspect the Original Image**

   ```python
   cv2.imshow('Citra Asli', img)
   print('Nilai Sebelum Translasi', img)
   ```

   * `cv2.imshow('Citra Asli', img)`: Opens a window titled “Citra Asli” and shows the loaded image.
   * `print('Nilai Sebelum Translasi', img)`: Prints the raw pixel values (NumPy array) of the original image to the console.

4. **Obtain Image Dimensions**

   ```python
   num_rows, num_cols = img.shape[:2]
   ```

   * `num_rows`: height of the image in pixels.
   * `num_cols`: width of the image in pixels.
   * We only take the first two elements of `img.shape` to ignore the number of channels.

5. **Create the Translation Matrix**

   ```python
   translation_matrix = np.float32([ [1, 0, 70],
                                     [0, 1, 60] ])
   ```

   * This is a **2×3** affine transformation matrix for translation.
   * Format:

     ```
     [ 1   0   tx ]
     [ 0   1   ty ]
     ```

     where `tx = 70` (shift right by 70 pixels) and `ty = 60` (shift down by 60 pixels).

6. **Apply the Translation (Affine Warp)**

   ```python
   img_translation = cv2.warpAffine(
       img,
       translation_matrix,
       (num_cols, num_rows)
   )
   ```

   * `cv2.warpAffine` applies the affine transformation to each pixel in `img`.
   * The third argument `(num_cols, num_rows)` specifies the output image size (width, height).
   * Pixels shifted outside the image frame are discarded; empty regions become black by default.

7. **Display & Inspect the Translated Image**

   ```python
   print('Nilai Setelah Translasi', img_translation)
   cv2.imshow('Translasi Gambar', img_translation)
   cv2.waitKey()
   ```

   * `print('Nilai Setelah Translasi', img_translation)`: Prints the pixel array of the translated image.
   * `cv2.imshow('Translasi Gambar', img_translation)`: Shows the shifted image in a new window titled “Translasi Gambar”.
   * `cv2.waitKey()`: Waits indefinitely until any key is pressed, keeping the windows open.

---

### Full Code Listing

```python
import cv2
import numpy as np

img = cv2.imread(r'Foto\gambar.jpeg')

cv2.imshow('Citra Asli', img)
print('Nilai Sebelum Translasi', img)

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([ [1, 0, 70], [0, 1, 60] ])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))

print('Nilai Setelah Translasi', img_translation)
cv2.imshow('Translasi Gambar', img_translation)
cv2.waitKey()
```
