## Workflow of the Contrast Adjustment Script

1. **Import Libraries**

   ```python
   import cv2
   import numpy as np
   ```

   * **cv2**: OpenCV, for reading and displaying images.
   * **numpy**: Numerical operations on arrays.

2. **Load and Convert to Grayscale**

   ```python
   img = cv2.imread("Foto/gambar.jpeg")
   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ```

   * Read the color image from disk.
   * Convert it to a single-channel grayscale image (`0–255` intensity).

3. **(Optional) Print Original Matrix**

   ```python
   print("Original Image Array")
   print(img)
   ```

   * Displays the 2D array of pixel values in the console.

4. **Find Minimum and Maximum Intensities**

   ```python
   min_val = np.amin(img)
   max_val = np.amax(img)
   ```

   * `min_val`: darkest pixel in the image.
   * `max_val`: brightest pixel in the image.

5. **Prepare an Empty Output Array**

   ```python
   H, W = img.shape
   array_contrast = np.zeros((H, W), np.uint8)
   ```

   * `H, W`: image height and width.
   * `array_contrast`: will hold the contrast-stretched result.

6. **Loop Over Every Pixel & Stretch Contrast**

   ```python
   for i in range(H):
       for j in range(W):
           p = float(img[i, j])   # to prevent integer overflow
           # Linear stretch formula:
           p = (p - min_val) * 255 / (max_val - min_val)
           # Clip to [128, 255] to keep values in a restricted range
           array_contrast[i, j] = np.clip(p, 128, 255)
   ```

   * **Formula**:

     $$
       \text{new} = \frac{(\text{old} - \min)}{\max - \min} \times 255
     $$
   * **Clipping**: forces every pixel into the 128–255 range (you can adjust these bounds).

7. **(Optional) Print the Resulting Array**

   ```python
   print("Contrast-Adjusted Array")
   print(array_contrast)
   ```

8. **Display Before & After**

   ```python
   cv2.imshow("Before", img)
   cv2.imshow("After",  array_contrast)
   cv2.waitKey(0)          # Wait for any key
   cv2.destroyAllWindows() # Close windows
   ```

   * Opens two windows showing the original and contrast-stretched images side by side.

---

### Full Example

```python
import cv2
import numpy as np

# 1–2. Load and grayscale
img = cv2.imread("Foto/gambar.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Print original (optional)
print("Original Image Array")
print(img)

# 4. Find min/max
min_val = np.amin(img)
max_val = np.amax(img)

# 5. Prepare output
H, W = img.shape
array_contrast = np.zeros((H, W), np.uint8)

# 6. Contrast stretching
for i in range(H):
    for j in range(W):
        p = float(img[i, j])
        p = (p - min_val) * 255 / (max_val - min_val)
        array_contrast[i, j] = np.clip(p, 128, 255)

# 7. Print result (optional)
print("Contrast-Adjusted Array")
print(array_contrast)

# 8. Display
cv2.imshow("Before", img)
cv2.imshow("After",  array_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
