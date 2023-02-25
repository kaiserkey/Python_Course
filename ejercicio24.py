""" 
    Vamos a comprobar si un punto del plano cartesiano de la forma (x,y)
    pertenece o no al cuadrado unidad.
    
    El cuadrado unidad tiene los vertices (0,0), (0,1), (1,0) y (1,1).
"""

x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

if x >= 0 and x <=1 and y >=0 and y <=1:
    print(f"El punto ({x},{y}) pertenece al cuadrado unidad.")
else:
    print(f"El punto ({x},{y}) no pertenece al cuadrado unidad.")