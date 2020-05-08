from PIL import Image
imagen = Image.open("file.jpg")
 
# Aquí hacemos la conversión | Here we do the conversion
imagen.save("file.webp")

print("Done!")