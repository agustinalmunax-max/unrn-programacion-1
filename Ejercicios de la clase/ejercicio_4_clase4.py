opcion = ""
total = 0
menu = "pizza = 15$USD", "hamburguesa = 20$USD", "empanadas de carne = 10 $USD", "tarta de verduras = 5$USD", "milanesa napolitana = 25$USD"
print("Selecciona la comida para llevar. Para salir, escriba: terminar pedido")
print(menu)
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        total += 15
        print("Excelente! Agregamos una pizza a tu pedido")
    elif opcion == "tarta de verduras":
        total += 5
        print("Excelente! Agregamos una tarta de verduras a tu pedido")
    elif opcion == "empanadas de carne":
        total += 10
        print("Excelente! Agregamos unas empanadas de carne")
    elif opcion == "hamburguesa":
        total += 20
        print("Excelente! Agregamos una hamburguesa a tu pedido")
    elif opcion == "milanesa napolitana":
        total += 25
        print("Excelente! Agregamos una milanesa napolitana a tu pedido")
    elif opcion == "terminar pedido":
        print("Cerrando pedido")
    else:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")

print(f"pedido finalizado, el total es {total}$USD gracias por confiar en nosotros")