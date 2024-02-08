### Sets ###

# Definición

my_set = set() #MUTABLE, podemos añadir elementos
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) #es un set porque un dicc necesita clave y valor
print(len(my_other_set)) 

# Inserción

my_other_set.add("MoureDev")
print(my_other_set)  # Un set no es una estructura ordenada. Tampoco puedes acceder a ningun elemento porque cada vez está ordenado de una manera diferente

my_other_set.add("MoureDev")  # Un set no admite repetidos
print(my_other_set)

# Búsqueda

print("Moure" in my_other_set) #existe, true
print("Mouri" in my_other_set) #no existe, false

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear() #vacia elementos pero siguen existiendo
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined. DESAPARECE

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0]) #muy arriesgado porq nunca conoces el orden de los elementos

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) #ignora los primeros union porq no ducplica elementos
print(my_new_set.difference(my_set))

