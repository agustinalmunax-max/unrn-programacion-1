numeros = [4, 60, 200, 3000]

suma_total = 0
cantidad = 0

for n in numeros:
    suma_total = suma_total + n
    cantidad = cantidad + 1

promedio = suma_total / cantidad

print(f"Suma total: {suma_total}")
print(f"Cantidad de numeros: {cantidad}")
print(f"Promedio: {promedio}")