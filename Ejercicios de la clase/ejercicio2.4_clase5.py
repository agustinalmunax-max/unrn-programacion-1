def pedir_comida():
    comida = ""
    while comida == "":
       comida = input("Ingresa tu comida> ")
    return comida

print(pedir_comida())