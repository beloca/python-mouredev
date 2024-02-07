### Exception Handling ##Manejo de errores#

numberOne = 5
numberTwo = 1
numberTwo = "1"
#si aqui hiciesemos print y sumamos el numberOne y nomberTwo da error porq no puede sumar dato y string

# Excepción base: try except

try:
    print(numberOne + numberTwo) #esta linea da error por lo que se ajecuta except
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: #se ejecuta sólo si produce este error de value
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: #la palabra error puede ser lo que tu pongas
    print(error)
except Exception as my_random_error_name: #esto es una excepcion generica
    print(my_random_error_name)
#se cumple la exception porq valueerror no se cumple