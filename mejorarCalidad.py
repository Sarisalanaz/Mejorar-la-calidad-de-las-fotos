from PIL import Image, ImageFilter

def mejorar_calidad_png(input_path, output_path):
    # Cargar la imagen
    imagen = Image.open(input_path)

    # Aplicar un filtro de mejora (aquí usamos un filtro de aumento de nitidez)
    imagen_mejorada = imagen.filter(ImageFilter.SHARPEN)

    # Guardar la imagen mejorada
    imagen_mejorada.save(output_path)

# Ruta del archivo de entrada y salida
input_path = 'wepik.png'  # Cambia esto por la ruta de tu imagen
output_path = 'imagen_mejorada.png'  # Nombre del archivo de salida

# Llama a la función para mejorar la calidad de la imagen
mejorar_calidad_png(input_path, output_path)