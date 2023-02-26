""" 
    Realizar un ciclo while para hacer una cuenta atras
    
    import time
    time.sleep(1)

    Esta línea de código usa la función time.sleep () para hacer que el programa 
    se detenga por un segundo. Esto se utiliza a menudo para hacer que el programa 
    espere un cierto período de tiempo antes de realizar la acción siguiente.
"""
import time 

cuenta = 10

while cuenta > 0: 
    print(cuenta)
    time.sleep(1)
    cuenta -= 1
else:
    time.sleep(1)
    print("...")
    print("¡BOOO!")