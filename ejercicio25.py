""" 
    Comprobar si un año es bisiesto o no.
    
    Un año es bisiesto si es divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
"""

year = int(input("Ingrese un año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")