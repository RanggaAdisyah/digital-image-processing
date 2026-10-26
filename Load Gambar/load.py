from PIL import Image

CITRA = Image.open('Foto/gambar.jpeg')
PIXEL = CITRA.load()

CITRA.save('hasil_load.jpeg')