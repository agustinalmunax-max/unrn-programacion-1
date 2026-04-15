productos = ["Papa", "Manzana","Zanahoria", "Cebolla", "Naranja" ]
cantidad = 0

for producto in productos:
    cantidad = cantidad + 1
    primero = productos[0]
    ultimo = productos[cantidad - 1]

print(f"Cantidad de productos: {cantidad}")
print(f"El primero: {primero}")
print(f"El ultimo: {ultimo}")