from PIL import Image

# Membuka gambar
CITRA = Image.open('Foto/gambar.jpeg')

# Mengonversi gambar menjadi grayscale
CITRA_GRAYSCALE = CITRA.convert('L')

# Mengambil ukuran gambar
ukuran_horizontal = CITRA_GRAYSCALE.size[0]
ukuran_vertikal = CITRA_GRAYSCALE.size[1]

# Memuat piksel grayscale
PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

# Memodifikasi nilai piksel (misalnya, di koordinat (3, 8))
PIXEL_GRAYSCALE[3, 8] = 128

# Menampilkan nilai piksel setelah diubah
print(PIXEL_GRAYSCALE[3, 8])

# Menyimpan hasil gambar grayscale
CITRA_GRAYSCALE.save('Grayscale/hasil_grayscale1.jpeg')
