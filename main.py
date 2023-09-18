from rembg import remove
from PIL import Image

input_path = 'lince.jpg' # Agregamos la ruta de la image
output_path = 'output.png' # Inicializamos variable para el resultado esperado
input = Image.open(input_path) # Obtenempos la variable de la imagen 
output = remove(input) # Removemos el fondo de la imagen 
output.save(output_path) # Guardamos el resultado esperado