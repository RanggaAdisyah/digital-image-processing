## Workflow of the Two-Image Subtraction Script

### Prerequisites

* **Python 3.x** installed
* **Pillow** library (PIL fork) installed via:

  ```bash
  pip install pillow
  ```
* Two input images (`gambar1.jpeg` and `gambar2.jpeg`) of **the same dimensions** in your working directory.

---

### Step-by-Step Guide

1. **Import the Image Module**

   ```python
   from PIL import Image
   ```

   Provides the tools to open, manipulate, and save images.

2. **Define the Subtraction Function**

   ```python
   def pengurangan_dua_citra(citra_A, citra_B, citra_hasil):
   ```

   * **Parameters**:

     * `citra_A`, `citra_B`: file paths of the two source images.
     * `citra_hasil`: file path for saving the output.

3. **Open & Convert to RGB**

   ```python
   CITRA_A = Image.open(citra_A).convert('RGB')
   CITRA_B = Image.open(citra_B).convert('RGB')
   ```

   * Ensures each image has three color channels (R, G, B).

4. **Retrieve Image Dimensions**

   ```python
   ukuran_horizontal = CITRA_A.size[1]
   ukuran_vertikal = CITRA_A.size[1]
   ```

   * Both images must share `width` and `height`.

5. **Load Pixel Access Objects**

   ```python
   PIXEL_A = CITRA_A.load()
   PIXEL_B = CITRA_B.load()
   ```

   * Allows reading/writing individual pixels by `(x, y)`.

6. **Create the Output Image**

   ```python
   CITRA_HASIL = Image.new('RGB', (ukuran_horizontal, ukuran_vertikal))
   PIXEL_HASIL = CITRA_HASIL.load()
   ```

   * Initializes a blank RGB image the same size as the inputs.

7. **Subtract Pixel Values**

   ```python
   for x in range(ukuran_horizontal):
       for y in range(ukuran_vertikal):
           r = abs(PIXEL_A[x, y][0] - PIXEL_B[x, y][0])
           g = abs(PIXEL_A[x, y][1] - PIXEL_B[x, y][1])
           b = abs(PIXEL_A[x, y][2] - PIXEL_B[x, y][2])
           PIXEL_HASIL[x, y] = (r, g, b)
   ```

   * For each pixel coordinate:

     * Compute the absolute difference for each channel (R, G, B).
     * Store the result in the corresponding pixel of the output image.

8. **Save the Result**

   ```python
   CITRA_HASIL.save(citra_hasil)
   print(f"Subtraction result saved as {citra_hasil}")
   ```

   * Writes out the difference image to disk.

---

### Example Usage

```python
from PIL import Image

# Function definition as above...

# Run subtraction on two images:
pengurangan_dua_citra(
    'gambar1.jpeg',     # First source image
    'gambar2.jpeg',     # Second source image
    'hasil_pengurangan.jpeg'  # Output filename
)
```

After running this script, `hasil_pengurangan.jpeg` will contain the absolute pixel-by-pixel differences between `gambar1.jpeg` and `gambar2.jpeg`. This technique is useful for motion detection, change detection, or highlighting differences between two similar images.
