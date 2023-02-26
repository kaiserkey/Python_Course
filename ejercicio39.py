n = int(input("Ingrese un número entero para mover la rueda del abcdario: "))

i = 65

while i <= 90:
    if i + n <= 90:
        print(f"La letra {chr(i)} se ha movido: {chr(i+n)}")
    else: 
        print(f"La letra {chr(i)} se ha movido: {chr(n+(i-26))}")
    i += 1
else:
    print("Fin del programa")
    
