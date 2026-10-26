## Workflow of the Mean-Filter Smoothing Script

1. **Import Required Libraries**

   ```python
   import cv2
   import numpy as np
   from matplotlib import pyplot as plt
   ```

   * **cv2** for image I/O and filtering
   * **numpy** for kernel definition and array operations
   * **matplotlib** for displaying results side by side

2. **List the Input Images**

   ```python
   image_paths = [
     r'Foto\1.jpg',
     r'Foto\2.jpg',
     r'Foto\3.jpg'
   ]
   ```

   * Change these paths to point at your own files.

3. **Define the Smoothing Kernel**

   * **Uniform mean filter (each weight = 1/9):**

     ```python
     mean = np.array([
       [0.111, 0.111, 0.111],
       [0.111, 0.111, 0.111],
       [0.111, 0.111, 0.111]
     ])
     ```
   * **Weighted mean (Gaussian-like) filter:**

     ```python
     mean = np.array([
       [0.0625, 0.125 , 0.0625],
       [0.125 , 0.25  , 0.125 ],
       [0.0625, 0.125 , 0.0625]
     ])
     ```
   * You can swap these kernels in your code to compare results.

4. **Prepare a Matplotlib Grid**

   ```python
   fig, axs = plt.subplots(
     len(image_paths), 2,
     figsize=(10, 12)
   )
   ```

   * Creates a canvas with one row per image and two columns (original vs. smoothed).

5. **Process Each Image**

   ```python
   for i, path in enumerate(image_paths):
       # a) Load and convert to grayscale
       I   = cv2.imread(path)
       img = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
       
       # b) Apply the mean filter
       im = cv2.filter2D(img, -1, mean)
       
       # c) Plot original
       axs[i, 0].imshow(img, cmap='gray')
       axs[i, 0].set_title(f'Original Image {i+1}')
       axs[i, 0].axis('off')
       
       # d) Plot smoothed
       axs[i, 1].imshow(im, cmap='gray')
       axs[i, 1].set_title(f'Smoothed Image {i+1}')
       axs[i, 1].axis('off')
   ```

6. **Finalize and Show**

   ```python
   plt.tight_layout()  # avoid overlap
   plt.show()          # display all figures
   ```

---

### How It Works

* **Reading & Grayscaling**
  Each color image is loaded from disk and converted to single‐channel grayscale so we only deal with intensity values (0–255).

* **Filter Definition**
  A 3×3 kernel describes how each output pixel is computed from its 3×3 neighborhood.

  * In the **uniform** case, all neighbors contribute equally (simple blur).
  * In the **weighted** case, the center and its immediate neighbors count more (smoother, less blocky).

* **Convolution via `filter2D`**
  OpenCV’s `filter2D` slides the kernel over the image, performing the weighted sum at each location. The result is a locally averaged (smoothed) version.

* **Visualization**
  Matplotlib displays the original and filtered images side by side for easy comparison.
