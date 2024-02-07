### Modules, como libreria. Codigo externo que queremos usar ###
#para importar modulos no se puede usar num.: 10_functions da error, no lo importa

from math import pi as PI_VALUE #libreria de propio python
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1) #com le hemos llamado de manera concreta en el import, ya no necesitas llamar al modulo
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)