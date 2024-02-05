### Functions ###

# Definición, resuelve probl concreto q nosotros vamos a indicar. 

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value, second_value): #parametros q queremos pasar.
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7") #si pusiesemos division, aqui daría error porq es string
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result) #no retorna nada: NONE

my_result = sum_two_values_with_return(10, 5)
print(my_result) #el resultado queda guardado en nuestra ueva variable

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"): #el valor por defecto de alias, si alguien no lo mete sale "sin alias"
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts): #el asterisco hace q sea dinamico, puedes psar un texto, 3 o 20
    print(type(texts))
    for text in texts: #para poder hacer mayusculas, y como si hiciesemos una lista infinita
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")