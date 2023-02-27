numbers = [0,1,1,2,2,2,3,3,3,3]

counted = []

for element in numbers:
    if element not in counted:
        counted.append(element)
        print(f"El elemento {element}, aparece {numbers.count(element)} en la lista")
else: 
    print("Fin de la lista")
    print(counted)