
sum = 1+2
product = sum * 2
print(f"La suma es: {sum}, el producto: {product}")

print("show this in the console")

#tipos de datos
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string 

#type() function to check the type of a variable
print(type(distance_to_alpha_centauri)) ## <class 'float'>

#Operadores aritméticos
# +, -, *, /, //, %, **
# // es la división entera
# % es el módulo
# ** es la potencia
#ejemplos
print(2+2) # 4
print(2-2) # 0
print(2*2) # 4
print(2/2) # 1.0
print(2//2) # 1
print(2%2) # 0
print(2**2) # 4

#Operadores de comparación
# ==, !=, <, >, <=, >=
#ejemplos
print(2==2) # True
print(2!=2) # False
print(2<2) # False
print(2>2) # False
print(2<=2) # True
print(2>=2) # True

#Operadores lógicos
# and, or, not
#ejemplos
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False) # False
print(not True) # False

#Operadores de asignación
# =, +=, -=, *=, /=, //=, %=, **=
#ejemplos
a = 2
a += 2 # a = a + 2
print(a) # 4
a -= 2 # a = a - 2
print(a) # 2
a *= 2 # a = a * 2
print(a) # 4
a /= 2 # a = a / 2
print(a) # 2.0
a //= 2 # a = a // 2
print(a) # 1.0
a %= 2 # a = a % 2
print(a) # 1.0
a **= 2 # a = a ** 2
print(a) # 1.0

#Operadores de identidad
# is, is not
#ejemplos
print(2 is 2) # True
print(2 is not 2) # False

#Operadores de pertenencia
# in, not in
#ejemplos
print("a" in "hola") # True
print("a" not in "hola") # False

#fechas
from datetime import date
print("Today's date is: " + str(date.today()))#imprime la fecha actual
