### Loops ### bucle. Repite, ejecuta vrias veces el mismo codigo

# While, siempre lleva condición

my_condition = 0

while my_condition < 10:   #el bucle para cuando llega a 10(<10) porq le hemos dicho q incremente en dos
    print(my_condition)
    my_condition += 2 #cada vez que entra en el bucle lo incremente en dos

else:  # Es opcional (cuando deja de cumplirse el while nos imprime este)
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break #paramos el bucle aunque el while siga cumpliendose
    print(my_condition)

print("La ejecución continúa")

# For, para listado de elementos. se repite tantas veces como elementos tengamos iterados

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #cada vez que entra en este for, imprime cada uno de os elementos
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict: #imprime las keys, no los values(my_dict.values(), te imprime valores)
    print(element)
    if element == "Edad":
        break #al llegar a edad para y no imprime 1, q es el ultio elemento
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue #no se usa, no aconsejable hoy en dia
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")