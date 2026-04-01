salir = True
i = 0
while True:
    print(f"Hola mundo, estoy en la iteración: {i}")
    i += 1
    if input("Ir a la proximma iteración? [si/no]") == "si":
        # salir = False
        #break
        continue
    if input("Desea salir? [si/no]") == "si":
        salir = False
        break
    print(f"Estoy al final de la iteración: {i-1}")
print("Adios")