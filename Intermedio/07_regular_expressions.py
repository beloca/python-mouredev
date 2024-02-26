### Regular Expressions ###
#comporbar si una cadena de texto tiene ciertos elementos

import re #regular expression

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match) #match busca desde le ppio, si pones "numero 7" imprime None aunque si lo contenga
start, end = match.span() #nos da el (0 , 18)q son los caracteres
print(my_string[start:end]) #accedemos solo a este trozo de string

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search, encuentra la primera ocurrencia

search = re.search("lección", my_string, re.I) #I ignora si esta en mayuscula o minuscula
print(search)
start, end = search.span() 
print(my_string[start:end])

# findall, encuentra todas y las pone en array []

findall = re.findall("lección", my_string, re.I)
print(findall)

# split, crea una lista de los valores antes y despues del patron que hemos dicho;

print(re.split(":", my_string)) #antes de los : y despues

# sub, sustituir

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Clase en vídeo (09/11/22): https://www.twitch.tv/videos/1648023317

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string)) #findall no tiene en cuenta los caracteres no numericos y si los numericos
#por eso imprime un 7
pattern = r"\D" #todas la letras menos el 7
print(re.findall(pattern, my_string)) 

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" 
#cadena de texto q empiece por ...todo lo q hemos puesto: de a-z de 0-9 @...
# + \ que es para escapar ciertos caracteres y el . es cualquier caracter menos lo del corchete
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))