# from PIL import Image


# def crop_image(image_path, output_path, x, y, width, height):
#     # Load the image
#     image = Image.open(image_path)

#     # Crop the image
#     cropped_image = image.crop((x, y, x + width, y + height))

#     # Save the cropped image
#     cropped_image.save(output_path)


# # Meminta pengguna untuk memasukkan jalur gambar input
# input_image_path = input("Masukkan jalur gambar input: ")

# # Meminta pengguna untuk memasukkan koordinat dan dimensi potongan gambar
# x = int(input("Masukkan nilai x: "))
# y = int(input("Masukkan nilai y: "))
# width = int(input("Masukkan lebar potongan: "))
# height = int(input("Masukkan tinggi potongan: "))

# # Meminta pengguna untuk memasukkan jalur gambar output
# output_image_path = input(
#     "Masukkan jalur untuk menyimpan gambar hasil potongan: ")

# crop_image(input_image_path, output_image_path, x, y, width, height)


from PIL import Image


def crop_image(image_path, output_path, x, y, width, height):
    # Load the image
    image = Image.open(image_path)

    # Crop the image
    cropped_image = image.crop((x, y, x + width, y + height))

    # Save the cropped image
    cropped_image.save(output_path)


# Contoh penggunaan
input_image_path = '1141541.jpg'
output_image_path = 'hasil_cropped.png'
x = 100  # Koordinat x kiri atas
y = 100  # Koordinat y kiri atas
width = 200  # Lebar gambar yang dipotong
height = 200  # Tinggi gambar yang dipotong

crop_image(input_image_path, output_image_path, x, y, width, height)
