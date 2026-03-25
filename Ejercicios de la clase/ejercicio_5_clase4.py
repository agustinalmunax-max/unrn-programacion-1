lista_de_super = [
    "Huevos",
    "Pan",
    "Coca",
    "Azúcar",
    "Leche",
    "Fideos"
]

print(type(lista_de_super))

for indice in range(1, len(lista_de_super)):
    #print(indice)
    #print(lista_de_super[indice])
    print(f"(indice+1): (lista_de_super[indice])")
    
indice = 0
while indice < len(lista_de_super):
    print(indice, lista_de_super[indice])
    indice += 1

while True:
    indice_seleccionado = int(input("Elegi el producto"))
    if indice_seleccionado < len(lista_de_super):
        producto = lista_de_super[indice_seleccionado]
        print(f"Elegiste el indice (indice_seleccionado): {producto}")
    else:
        print("elegiste un producto invalido")