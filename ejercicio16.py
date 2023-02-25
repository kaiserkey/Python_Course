""" 
    Variables booleanas y operaciones de decision
"""

is_adult = True 
type(is_adult)

#Tabla de la verdad para una expresión OR

"""
Una expresión OR(Disyuncion / ∨) compara dos valores lógicos (True o False) y devuelve True si al menos uno de los dos valores es True.

A         | B        | OR
-------------------------
True     | True     | True
True     | False    | True
False    | True     | True
False    | False    | False

"""

#Ejemplo de una expresión OR
A = True
B = False

if A or B:
    print("True")
else:
    print("False")

# Salida: True

"""
Una expresión AND(Conjuncion / ∧) compara dos valores lógicos (True o False) y devuelve True solo si ambos valores son True.

Valor 1  | Valor 2  | AND
-------------------------
True     | True     | True
True     | False    | False
False    | True     | False
False    | False    | False

"""

#Ejemplo de una expresión AND


A = True
B = False

if A and B:
    print("True")
else:
    print("False")

#Salida: False

"""
Una expresión NOT toma un único valor lógico (True o False) y lo invierte.

Valor    | NOT
----------------
True     | False
False    | True

"""

#Ejemplo de una expresión NOT


A = True

if not A:
    print("True")
else:
    print("False")

#Salida: False


