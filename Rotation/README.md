## Workflow of the Image Rotation Script

### Prerequisites

* **Python 3.x** installed
* **OpenCV** library installed via:

  ```bash
  pip install opencv-python
  ```
* An input image file (e.g., `Foto/gambar.jpeg`) accessible by your script.

---

### Step-by-Step Guide

1. **Import OpenCV**

   ```python
   import cv2
   ```

   * Provides image I/O and geometric transformation functions.

2. **Load the Source Image**

   ```python
   img = cv2.imread(r'Foto\gambar.jpeg')
   ```

   * Reads the image into a NumPy array `img` of shape `(height, width, channels)` in BGR color order.

3. **Display & Inspect the Original**

   ```python
   cv2.imshow('Original Image', img)
   print('Original Image Array:', img)
   cv2.waitKey(0)
   ```

   * `imshow` opens a window titled “Original Image.”
   * `print` dumps the raw pixel array to the console for debugging.
   * `waitKey(0)` pauses until a key is pressed, then you can close the window.

4. **Compute Image Center**

   ```python
   num_rows, num_cols = img.shape[:2]
   center = (num_cols / 2, num_rows / 2)
   ```

   * `num_rows`: image height in pixels.
   * `num_cols`: image width in pixels.
   * `center`: rotation pivot at the geometric center.

5. **Build the Rotation Matrix**

   ```python
   # For 90° rotation:
   angle = 90
   scale = 1.0
   M = cv2.getRotationMatrix2D(center, angle, scale)
   ```

   * `getRotationMatrix2D` returns a 2×3 affine matrix that encodes rotation about `center`, by `angle` degrees, scaled by `scale`.

6. **Apply the Affine Warp**

   ```python
   rotated_90 = cv2.warpAffine(img, M, (num_cols, num_rows))
   ```

   * `warpAffine` applies the rotation matrix `M` to every pixel.
   * The output size is kept the same as the original: `(width, height)`.

7. **Display & Inspect the Rotated Image**

   ```python
   print('Rotated 90° Array:', rotated_90)
   cv2.imshow('Rotated 90°', rotated_90)
   cv2.waitKey(0)
   ```

8. **Repeat for 180° Rotation**

   ```python
   # Recompute matrix for 180°
   angle = 180
   M = cv2.getRotationMatrix2D(center, angle, scale)
   rotated_180 = cv2.warpAffine(img, M, (num_cols, num_rows))

   print('Rotated 180° Array:', rotated_180)
   cv2.imshow('Rotated 180°', rotated_180)
   cv2.waitKey(0)
   ```

9. **Cleanup Windows**

   ```python
   cv2.destroyAllWindows()
   ```

   * Closes all OpenCV display windows.

---

### Full Example

```python
import cv2

# 1. Load image
img = cv2.imread(r'Foto\gambar.jpeg')

# 2. Show original
cv2.imshow('Original Image', img)
print('Original Image Array:', img)
cv2.waitKey(0)

# 3. Get dimensions and center
num_rows, num_cols = img.shape[:2]
center = (num_cols / 2, num_rows / 2)
scale = 1.0

# 4. Rotate 90°
M90 = cv2.getRotationMatrix2D(center, 90, scale)
rotated_90 = cv2.warpAffine(img, M90, (num_cols, num_rows))
print('Rotated 90° Array:', rotated_90)
cv2.imshow('Rotated 90°', rotated_90)
cv2.waitKey(0)

# 5. Rotate 180°
M180 = cv2.getRotationMatrix2D(center, 180, scale)
rotated_180 = cv2.warpAffine(img, M180, (num_cols, num_rows))
print('Rotated 180° Array:', rotated_180)
cv2.imshow('Rotated 180°', rotated_180)
cv2.waitKey(0)

# 6. Cleanup
cv2.destroyAllWindows()
```
