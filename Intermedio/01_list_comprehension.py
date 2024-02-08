### List Comprehension ### listas comprimidas,crear listas en base a las q ya tenemos

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8) #rango de 8 para que coja todad la lista
print(list(my_range))

# Definición. La i se corresponde con cada uno de los elementos
my_list = [i + 1 for i in range(8)] #i for i in..palabras reservadas de python para acceder a otra lista concreta
print(my_list) #a cada elemento le esta sumando 1

my_list = [i * 2 for i in range(8)]
print(my_list) #el doble de cada uno de los valores

my_list = [i * i for i in range(8)] #que se multiplique por sí mismo
print(my_list)

def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in range(8)]
print(my_list)