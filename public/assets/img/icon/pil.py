from PIL import Image
import os

input_image = Image.open(
    "C:/Users/Administrator/Documents/GitHub/ABEPE/public/assets/img/icon/attendifylogo.png")
sizes = [(72, 72), (96, 96), (128, 128), (144, 144),
         (152, 152), (192, 192), (384, 384), (512, 512)]

for size in sizes:
    output_image = input_image.resize(size)
    file_name = str(size[0]) + "x" + str(size[1]) + ".png"
    output_image.save(file_name)
    print("Saved ", file_name)

print("All output images saved.")
