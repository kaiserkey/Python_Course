""" 
    Con un bucle for, dada una progresion aritmetica de numeros enteros indicada por
    el usuario, nos dara el primer termino, la diferencia y la cota. Vamos a calcular
    la suma de los elementos incluyendo la cota. 
"""

terminoInicial = int(input("Introduce el primer termino: "))
diferencia = int(input("Introduce la diferencia: "))
cota = int(input("Introduce la cota para finalizar: "))

sumatoria = 0

for i in range(terminoInicial, cota+1, diferencia):
    sumatoria = sumatoria + i

print("La sumatoria de los elementos es: ", sumatoria)