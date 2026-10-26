## Workflow of the Histogram Equalization Script

1. **Import Required Libraries**

   ```python
   import cv2
   import numpy as np
   from matplotlib import pyplot as plt
   ```

   * **cv2**: OpenCV, for image I/O and color conversion.
   * **numpy**: Array operations and histogram calculation.
   * **matplotlib.pyplot**: Plotting images and histograms.

2. **Define the Equalization Function**

   ```python
   def histogram_equalize(A):
       bins = 256
       A = A + 1  # shift pixel values to 1–256 to avoid zero index
       # Compute histogram
       freq, _ = np.histogram(A, bins=bins)
       # Compute cumulative histogram
       cum_hist = freq.cumsum()
       # Map old intensities to new ones in [0,255]
       prob = np.round((cum_hist / float(A.size)) * (bins - 1))
       # Create output image
       B = np.empty(A.shape)
       rows, cols = A.shape
       for i in range(rows):
           for j in range(cols):
               B[i, j] = prob[int(A[i, j]) - 1]
       return B
   ```

   * **Step-by-step inside the function**:

     1. **Shift** pixel values to avoid zero indexing
     2. **Compute frequencies** of each gray level with `np.histogram`
     3. **Accumulate** to get the cumulative distribution (`cum_hist`)
     4. **Normalize** and **scale** to `[0,255]` to form the lookup table `prob`
     5. **Remap** every pixel in the input image `A` via this table to produce the equalized image `B`.

3. **Load and Grayscale the Images**

   ```python
   I1 = cv2.imread(r'Pemerataan\1.jpg')
   gray1 = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
   # Repeat for I2→gray2 and I3→gray3
   ```

   * Reads three photos with different original contrast levels.
   * Converts each from BGR color to single-channel grayscale.

4. **Apply Histogram Equalization**

   ```python
   result1 = histogram_equalize(gray1)
   result2 = histogram_equalize(gray2)
   result3 = histogram_equalize(gray3)
   ```

   * Each `gray` image is fed into `histogram_equalize`, producing a contrast-stretched version.

5. **Display Original vs. Equalized Images**

   ```python
   fig1, axs1 = plt.subplots(3, 2, figsize=(10, 10))
   fig1.suptitle('Histogram Equalization on Three Images')

   # Row 1: high-contrast image
   axs1[0, 0].imshow(gray1, cmap='gray');      axs1[0, 0].set_title('Original – High Contrast')
   axs1[0, 1].imshow(result1, cmap='gray');    axs1[0, 1].set_title('Equalized – High Contrast')
   # Row 2: medium contrast, Row 3: low contrast (similar code)

   for ax in axs1.ravel():
       ax.axis('off')

   plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
   plt.show()
   ```

   * Creates a **3×2 grid**:

     * Left column: original grayscale images
     * Right column: their equalized counterparts
   * Titles indicate whether the source had high, medium, or low contrast.

6. **Plot Histograms of the Equalized Results**

   ```python
   fig2, axs2 = plt.subplots(1, 3, figsize=(15, 5))
   fig2.suptitle('Histograms After Equalization')

   axs2[0].hist(result1.ravel(), 256, [0, 256]); axs2[0].set_title('High Contrast')
   axs2[1].hist(result2.ravel(), 256, [0, 256]); axs2[1].set_title('Medium Contrast')
   axs2[2].hist(result3.ravel(), 256, [0, 256]); axs2[2].set_title('Low Contrast')
   for ax in axs2:
       ax.set_xlim([0, 255])

   plt.tight_layout(rect=[0, 0, 1, 0.90])
   plt.show()
   ```

   * For each equalized image, flattens the pixel array with `.ravel()`, then plots a **256-bin histogram**.
   * Shows how the pixel intensities are redistributed across the full range after equalization.

---
