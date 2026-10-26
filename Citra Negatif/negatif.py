from PIL import Image

CITRA = Image.open('Foto\\gambar.jpeg')

ukuran_horizontal = CITRA.size[0]
ukuran_vertikal = CITRA.size[1]

PIXEL = CITRA.load()

for x in range(ukuran_vertikal):
    for y in range(ukuran_horizontal):
        R = 255 - PIXEL[y, x][0]
        G = 255 - PIXEL[y, x][1]
        B = 255 - PIXEL[y, x][2]
        PIXEL[y, x] = (R, G, B)
        
CITRA.save('hasil_negatif.jpeg')
        