temperatura = int(input("Ingrese su temperatura actual en °C: "))
abrigo = False
ropa_media = False
ropa_liviana = False

if temperatura > 20:
    abrigo = True
    print("Usted esta usando abrigo")
elif 10 <= temperatura <= 20:
    ropa_media = True
    print("usted esta usando ropa media")
else:
    ropa_liviana = True
    print("usted esta usando ropa liviana")