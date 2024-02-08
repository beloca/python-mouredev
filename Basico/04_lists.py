### Lists, ###

# Definición

my_list = list() #conjunto valores MUTABLES
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) #las veces q se repite
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev") #añade al final
print(my_other_list)

my_other_list.insert(1, "Rojo") #le dices en q posición añadirle el valor
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul") #eliminamos
print(my_other_list)

my_list.remove(30) #elimina el primero de los dos valores 30
print(my_list)

print(my_list.pop()) #elimina ultimo elemento y es lo que te duvuelve (17)
print(my_list)

my_pop_element = my_list.pop(2) #imprime 62 q seria el q elimina y lo hemos guardado en una variable nueva
print(my_pop_element)
print(my_list)

del my_list[2] #borra el elemento del indice q le digas
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() #copia

my_list.clear() #elimina
print(my_list)
print(my_new_list)

my_new_list.reverse() #da la vuelta a la lista
print(my_new_list)

my_new_list.sort() #puedes dar criterios para ordenar, o lo ordena el por defecto > o <
print(my_new_list)

# Sublistas

print(my_new_list[1:3]) #como los strings, son sublistas

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))