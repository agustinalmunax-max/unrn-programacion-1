def pedir_comida():
    comida = ""
    while comida == "":
       comida = input("Ingresa tu comida> ")
    return comida

def obtener_precio(comida):
    precio = 0
    if comida == "hamburguesa":
        print("hamburguesa 100$")
        precio = 100
    elif comida == "milanesa":
        print("milanesa 125$")
        precio = 125
    elif comida == "pizza":
        print("pizza 150$")
        precio = 150
    else:
        print("lo sentimos, no tenemos")
    return precio
    
comida = pedir_comida()
print(obtener_precio(comida))