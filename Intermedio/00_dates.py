### Dates ###

# Date time, agrupa fecha y hora

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now() #dentro del modulo queremos acceder a esta operacion

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) #representacion unica desde 1970

print_date(now)
 
year_2023 = datetime(2023, 1, 1) #año, mes, día, lo minimo q necesitamos para definirlo
#nos imprime cero en hora minuto y seg porq no lo hemos definido
print_date(year_2023)

# Time, solo hora

current_time = time(21, 6, 0) #nos sirve para encapsular tiempo. hay q pasar objetos

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date, solo fecha

current_date = date.today() #podemos definirlo nosotros (año.mes.dia) 

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,current_date.month + 1, current_date.day)

print(current_date.month) #imprime 11 porque hemos hecho +1

# Operaciones con fechas

diff = year_2023 - now #diff de diferencia. entre variable year_2023 y now (los dos son daos datetime)
print(diff)

diff = year_2023.date() - current_date #ahora con date. Los objetos deben ser del mismo tipo
print(diff)

# Timedelta, opera con diferencias de fechas. Para trabajar con franjas de fechas

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
