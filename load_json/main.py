import json
import requests


path_disco = "H:/INET-cisco/db_bases"
nombre_archivo = "provincias.json"
path_archivo = f"{path_disco}/{nombre_archivo}"
# Abre el archivo JSON en modo lectura ('r')
with open(path_archivo, 'r') as archivo_json:
    # Carga el contenido del archivo JSON en una variable Python
    datos = json.load(archivo_json)

# Ahora puedes trabajar con los datos como un diccionario o lista de Python
#print(type(datos))
    
print(datos["provincias"][0])


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)