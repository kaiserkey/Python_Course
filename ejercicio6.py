""" 
    Division entera o euclidea 
    Dado dos numeros naturales a y b, la division euclidea de a entre b
    es el cociente de la division entera de a entre b y el resto de la 
    division entera de a entre b.
    a = b.q + r
    r < b
"""

a = 10
b = 3

q = a // b

r = a % b

print("La division euclidea de a entre b es: ", q, " y el resto es: ", r, 
        " Quedando: ", a, "=", b, "*", q, "+", r, " Donde r < b")

