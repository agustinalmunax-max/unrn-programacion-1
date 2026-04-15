numeros = [4, 6, 12, 23, 14, 2, 7]

maximo = numeros[0]
minimo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n

print(f"El numero maximo es: {maximo}")
print(f"El numero minimo es: {minimo}")