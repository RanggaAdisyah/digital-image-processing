## Workflow of the Image Reflection Script

### Prerequisites

* **Python 3.x**
* **OpenCV** installed via:

  ```bash
  pip install opencv-python
  ```
* An input image at `Foto/gambar.jpeg` (or adjust the path as needed).

---

### Step-by-Step Guide

1. **Import OpenCV**

   ```python
   import cv2
   ```

   Provides functions for reading, displaying, and transforming images.

2. **Load the Source Image**

   ```python
   img = cv2.imread(r'Foto\gambar.jpeg')
   ```

   * Reads the image from disk into a NumPy array `img` of shape `(H, W, 3)` (BGR channels).

3. **Display & Inspect the Original**

   ```python
   cv2.imshow('Original Image', img)
   print('Original Image Array:', img)
   ```

   * `imshow` pops up a window titled “Original Image.”
   * `print` outputs the raw pixel values to the console for debugging or inspection.

4. **Perform Horizontal Reflection**

   ```python
   reflection_h = cv2.flip(img, 1)
   ```

   * `flipCode = 1` mirrors left↔right across the vertical axis.

5. **Display & Inspect the Horizontal Reflection**

   ```python
   print('Horizontally Reflected Array:', reflection_h)
   cv2.imshow('Horizontal Reflection', reflection_h)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

   * Shows the flipped image in a new window.
   * `waitKey(0)` pauses until any key is pressed; `destroyAllWindows` closes all windows.

6. **(Alternatively) Perform Vertical Reflection**

   ```python
   reflection_v = cv2.flip(img, 0)
   ```

   * `flipCode = 0` mirrors top↔bottom across the horizontal axis.

7. **Display & Inspect the Vertical Reflection**

   ```python
   print('Vertically Reflected Array:', reflection_v)
   cv2.imshow('Vertical Reflection', reflection_v)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

---

### Combined Example

```python
import cv2

# 1. Load image
img = cv2.imread(r'Foto\gambar.jpeg')

# 2. Show original
cv2.imshow('Original Image', img)
print('Original Image Array:', img)
cv2.waitKey(0)

# 3. Horizontal reflection (left↔right)
h_reflect = cv2.flip(img, 1)
print('Horizontally Reflected Array:', h_reflect)
cv2.imshow('Horizontal Reflection', h_reflect)
cv2.waitKey(0)

# 4. Vertical reflection (top↔bottom)
v_reflect = cv2.flip(img, 0)
print('Vertically Reflected Array:', v_reflect)
cv2.imshow('Vertical Reflection', v_reflect)
cv2.waitKey(0)

# 5. Cleanup windows
cv2.destroyAllWindows()
```
