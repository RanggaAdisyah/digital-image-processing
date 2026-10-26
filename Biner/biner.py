from PIL import Image

def citra_biner(nilai_ambang):
    CITRA_GRAYSCALE = Image.open('Foto/gambar.jpeg').convert('L')
    PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()
    
    ukuran_horizontal = CITRA_GRAYSCALE.size[0]
    ukuran_vertikal = CITRA_GRAYSCALE.size[1]
    
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            if PIXEL_GRAYSCALE[x, y] < nilai_ambang:
                PIXEL_GRAYSCALE[x, y] = 0
            else:
                PIXEL_GRAYSCALE[x, y] = 255
                
    hasil_biner = 'gambar_biner_' + str(nilai_ambang) + '.jpeg'
    CITRA_GRAYSCALE.save(hasil_biner)
    print(f"Gambar biner dengan ambang {nilai_ambang} telah disimpan sebagai {hasil_biner}")

# Panggil fungsi dengan nilai ambang yang berbeda
citra_biner(50)
citra_biner(128)
citra_biner(200)
