## Image Scaling with OpenCV

### 🧰 Requirements

* Python 3.x
* OpenCV library installed via:

  ```bash
  pip install opencv-python
  ```
* An image file located at `Foto/gambar.jpeg`

---

### 📌 Description

This script demonstrates how to **resize an image** using OpenCV by changing its width and height through a scaling factor.

---

### 🔄 Step-by-Step Workflow

1. **Import OpenCV**

   ```python
   import cv2
   ```

   * This imports the OpenCV library to handle image operations.

2. **Read the Image**

   ```python
   img = cv2.imread(r'Foto\gambar.jpeg')
   ```

   * Loads the image from disk into a NumPy array.
   * The image is loaded in BGR format.

3. **Display the Original Image**

   ```python
   cv2.imshow('Citra Asli', img)
   print('Nilai Citra Asli', img)
   ```

   * Shows the original image in a window titled "Citra Asli".
   * Prints the pixel values (array) to the console.

4. **Get Image Dimensions**

   ```python
   num_rows, num_cols = img.shape[:2]
   ```

   * Retrieves the height (`num_rows`) and width (`num_cols`) of the image.

5. **Define New Dimensions for Scaling**

   ```python
   new_rows, new_cols = int(num_rows * 2), int(num_cols * 0.5)
   ```

   * The height is **doubled**, and the width is **reduced by half**.
   * This creates a vertically stretched and horizontally compressed image.

6. **Resize the Image**

   ```python
   img_scaled = cv2.resize(img, (new_rows, new_cols))
   ```

   * Resizes the original image to the new dimensions.
   * `cv2.resize` takes size in the order `(width, height)` → so the arguments are swapped.

7. **Display the Scaled Image**

   ```python
   cv2.imshow('Hasil Skala', img_scaled)
   print('Nilai Citra Setelah Skala', img_scaled)
   ```

   * Shows the resized image in a new window titled "Hasil Skala".
   * Prints the pixel values of the resized image.

8. **Wait for a Key Press**

   ```python
   cv2.waitKey()
   ```

   * Pauses the execution and keeps the image window open until any key is pressed.

---

### 📝 Note

If the image does not display correctly or errors occur, make sure:

* The path `Foto/gambar.jpeg` exists and the file is accessible.
* The file is a supported image format (e.g., `.jpg`, `.png`).

---

### ✅ Output

* Two image windows:

  1. **Citra Asli** – original image.
  2. **Hasil Skala** – image resized to new dimensions.

This technique is useful for preprocessing, preparing datasets for machine learning, or optimizing images for different screen sizes.
