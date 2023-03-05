""" 
    Algoritmo que dado un numero lo exprese en numeros romanos
"""

#Definimos la funcion que nos permitira obtener el numero romano
def numero_romano(num):
    #Creamos una lista con los simbolos romanos
    romano = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    #Creamos otra lista con los numeros arabigos
    arabigo = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    #Definimos una variable que contendra el numero romano
    numero_romano = ''
    #Recorremos la lista arabigo
    for i in range(len(arabigo)):
        #Verificamos que el numero sea mayor o igual que el numero arabigo
        while num >= arabigo[i]:
            #Vamos agregando los numeros romanos a nuestra variable
            numero_romano += romano[i]
            #Le restamos al numero el numero arabigo
            num -= arabigo[i]
            #Retornamos el numero romano
    return numero_romano

#Pedimos al usuario que ingrese un numero
num = int(input('Ingrese un numero: '))

#Mostramos el resultado
print(numero_romano(num))


diccionario = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def obtenerRomano(numero):
    romano = ''
    for letra, valor in diccionario.items():
        # Repite la letra el número de veces indicado
        while numero >= valor:
            romano += letra
            numero -= valor
    return romano

print(obtenerRomano(num)) # Imprime V