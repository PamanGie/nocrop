import os
from PIL import Image
from tqdm import tqdm

def convert_images_in_folder(input_folder, output_folder, size):
    
    # Untuk membaca output folder, dibuat dulu ya folder outputnya masing-masing
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Untuk membaca file gambar, pastikan file gambar sesuai format yang dimasukkan
    image_files = [filename for filename in os.listdir(input_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Buat loading bar, biar keren ada animasinya
    progress_bar = tqdm(image_files, desc="Processing Images", unit="image")

    # Loop agar semua gambar dalam folder image agar setiap gambar di dalam folder menjadi gambar yang lebih rapi dan simetris
    for filename in progress_bar:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Panggil fungsi konversi untuk setiap gambar di folder
        convert_to_square(input_path, output_path, size)

    # Pesan ketika crop sudah selesai
    print("Successfully Cropped")

def convert_to_square(image_path, output_path, size):
    # Membuka gambar menggunakan Pillow
    original_image = Image.open(image_path)

    # Mendapatkan rasio aspek asli
    original_aspect_ratio = original_image.width / original_image.height

    # Menentukan dimensi baru sesuai dengan rasio aspek 1:1
    if original_aspect_ratio > 1:
        new_width = size
        new_height = int(size / original_aspect_ratio)
    else:
        new_width = int(size * original_aspect_ratio)
        new_height = size

    # Membuat gambar baru dengan latar belakang putih
    new_image = Image.new("RGB", (size, size), "white")

    # Menghitung posisi untuk menempatkan gambar asli di tengah
    x_offset = (size - new_width) // 2
    y_offset = (size - new_height) // 2

    # Menempatkan gambar asli di tengah dengan ukuran baru
    new_image.paste(original_image.resize((new_width, new_height), Image.ANTIALIAS), (x_offset, y_offset))

    # Menyimpan gambar hasil konversi
    new_image.save(output_path)

if __name__ == "__main__":
    # Masukkan nama folder input yang berisi gambar untuk di crop dan folder output hasilnya seperti dicontoh
    input_folder_path = "image"
    output_folder_path = "output"
    desired_size = 1125

    convert_images_in_folder(input_folder_path, output_folder_path, desired_size)
