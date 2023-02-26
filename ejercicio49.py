""" 
fechas en python

Python proporciona una variedad de módulos para trabajar con fechas y horas. El más común y versátil es el módulo datetime. Algunas de las funcionalidades que ofrece son: 

• Obtener la fecha y hora actual: datetime.now()
• Obtener una fecha y hora particular: datetime(year, month, day, hour, minute, second)
• Obtener una fecha y hora relativa a la actual: timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
• Obtener una representación de la fecha y hora en cadena: datetime.strftime(formato)
• Convertir una cadena de fecha a un objeto de fecha: datetime.strptime(cadena, formato)
• Añadir o restar días, semanas, horas, etc: datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
• Calcular el número de días entre dos fechas: datetime.date.days_in_month(year, month)

Ejemplos practicos:

• Obtener la fecha y hora actual:

import datetime

fecha_y_hora_actuales = datetime.datetime.now()
print(fecha_y_hora_actuales)

• Obtener una fecha y hora particular:

import datetime

fecha_y_hora_especificas = datetime.datetime(2020, 7, 16, 12, 0, 0)
print(fecha_y_hora_especificas)

• Obtener una fecha y hora relativa a la actual:

import datetime

fecha_y_hora_relativas = datetime.datetime.now() + datetime.timedelta(days=1, hours=2, minutes=30)
print(fecha_y_hora_relativas)

• Obtener una representación de la fecha y hora en cadena:

import datetime

fecha_y_hora_actuales = datetime.datetime.now()
fecha_y_hora_cadena = fecha_y_hora_actuales.strftime("%d-%m-%Y %H:%M:%S")
print(fecha_y_hora_cadena)

• Convertir una cadena de fecha a un objeto de fecha:

import datetime

cadena_fecha = "16-07-2020 12:00:00"
fecha_objeto = datetime.datetime.strptime(cadena_fecha, "%d-%m-%Y %H:%M:%S")
print(fecha_objeto)

• Añadir o restar días, semanas, horas, etc:

import datetime

fecha_y_hora_actuales = datetime.datetime.now()
fecha_y_hora_modificadas = fecha_y_hora_actuales + datetime.timedelta(days=7, hours=3, minutes=30)
print(fecha_y_hora_modificadas)

• Calcular el número de días entre dos fechas:

import datetime

fecha_inicio = datetime.datetime(2020, 7, 16)
fecha_fin = datetime.datetime(2020, 8, 16)
diferencia = fecha_fin - fecha_inicio
dias = diferencia.days
print(dias)
"""