### File Handling ###para manejar ficheros creamos my_file.txt
#tb podremos leer excel o csv

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermedio/my_file.txt", "w+")#la w es de write por escritura y + para hacer mas cosas
#para read y readline poner r+ en vez de w+
txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")
#\n cambia de linea
# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close() 

with open("Intermedio/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt") para eliminar el fichero

# Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# .json file. tipico en app web con el servidor


json_file = open("Intermedio/my_file.json", "w+")

json_test = { #la estructura es de diccionario
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"
    }

json.dump(json_test, json_file, indent=2) #3 argumentos; json, el archivo y la identación(forma en
#la que vamos a ver el archivo (los espacios) creado my_file.json. Si la quitamos nos pone archivo en una linea)

json_file.close()

with open("Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/my_file.json"))#transformarlo en un diccionario
print(json_dict)#lo imprime en esa estructura en una linea
print(type(json_dict))
print(json_dict["name"])

# .csv file
#es un archivo de texto que tiene un formato específico que permite guardar los datos en un formato de tabla estructurada.
#especie de excel
#si lo abres en numbres lo lee bien, en excel no
csv_file = open("Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?