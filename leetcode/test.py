import matplotlib.pyplot as plt

# Fungsi untuk membaca gambar PPM (format sederhana)
def read_ppm(filename):
    with open(filename, 'r') as f:
        # Membaca header
        magic_number = f.readline().strip()  # Format file (P3 untuk PPM)
        width, height = map(int, f.readline().split())  # Lebar dan tinggi gambar
        max_val = int(f.readline().strip())  # Nilai maksimum piksel (biasanya 255)

        # Membaca data piksel
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
        
        # Mengubah data piksel menjadi array 3D (height x width x 3)
        image = []
        for y in range(height):
            row = []
            for x in range(width):
                r = pixels[(y * width + x) * 3]
                g = pixels[(y * width + x) * 3 + 1]
                b = pixels[(y * width + x) * 3 + 2]
                row.append([r, g, b])
            image.append(row)
        return image

# Fungsi untuk menampilkan gambar
def show_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Membaca gambar
image = read_ppm('gambar.ppm')

# Menampilkan gambar
show_image(image)