numeros = [4, 6, 12, 23, 14, 2, 7]

for x in range(len(numeros)):
    numero_actual = numeros[x]
    if numero_actual % 2 == 0:
        print(f"El numero {numero_actual} es multiplo de 2")