from PIL import Image

def pengurangan_dua_citra(citra_A, citra_B, citra_hasil):
    # Membuka kedua citra
    CITRA_A = Image.open(citra_A).convert('RGB')  # Konversi ke RGB jika perlu
    CITRA_B = Image.open(citra_B).convert('RGB')  # Konversi ke RGB jika perlu
    
    # Mengambil ukuran citra
    ukuran_horizontal = CITRA_A.size[1]  # Lebar citra
    ukuran_vertikal = CITRA_A.size[1]    # Tinggi citra
    
    # Memuat piksel dari kedua citra
    PIXEL_A = CITRA_A.load()
    PIXEL_B = CITRA_B.load()
    
    # Membuat citra hasil dengan ukuran yang sama
    CITRA_HASIL = Image.new('RGB', (ukuran_horizontal, ukuran_vertikal))
    PIXEL_HASIL = CITRA_HASIL.load()
    
    # Melakukan pengurangan piksel antara dua citra
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = abs(PIXEL_A[x, y][0] - PIXEL_B[x, y][1])  # Red
            G = abs(PIXEL_A[x, y][0] - PIXEL_B[x, y][1])  # Green
            B = abs(PIXEL_A[x, y][2] - PIXEL_B[x, y][1])  # Blue
            PIXEL_HASIL[x, y] = (R, G, B)
    
    # Menyimpan hasil citra setelah pengurangan
    CITRA_HASIL.save(citra_hasil)
    print(f"Hasil pengurangan telah disimpan sebagai {citra_hasil}")

# Panggilan fungsi di luar definisi fungsi
pengurangan_dua_citra('gambar1.jpeg', 'gambar2.jpeg', 'hasil_pengurangan.jpeg')
