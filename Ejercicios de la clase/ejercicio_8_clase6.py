suma_total = 0
cantidad_de_numeros = 0

numero = int(input("Ingresá un número (o 0 para terminar): "))

while numero != 0:
    suma_total = suma_total + numero
    cantidad_de_numeros = cantidad_de_numeros + 1
    numero = int(input("Ingresá otro número (o 0 para terminar): "))

if cantidad_de_numeros > 0:
    promedio = suma_total / cantidad_de_numeros
    print(f"Suma total: {suma_total}")
    print(f"Cantidad de numeros: {cantidad_de_numeros}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron numeros para calcular.")