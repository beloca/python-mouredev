# Definición: todo lo q está dentro de la class tiene q responder a una cierta lógica
#la class persona tiene q tener relación con ella, por ej dormir pero no volar
#poder identificar nuestro codigo dentro de un ambito de actuación
#las clases siempre son en camello (mayuscula cada palabra) y no en snake case ( _ )

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"): #init nos sirve par crear constructor de clase. SIEMPRE SE LLAMA SELF
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada, al poner dos guines bajos se convierte en privado

    def get_name(self):
        return self.__name #creamos get para acceder a el pero no modificarla

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())# para poder acceder a la variable privada sin que se pueda modificar
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)" #se le puede cambiar el valor
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)