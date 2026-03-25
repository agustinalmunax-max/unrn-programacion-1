contraseña_ingresada = input("ingresar_contraseña: ")
contraseña_almacenada = "1234"
clave_token = bool(input("Usa clave token?") == "SI")

if contraseña_almacenada == contraseña_ingresada:
    acceso_permitido = True
    print("acceso con clave")
elif clave_token:
    print("acceso permitido con clave de token")
else:
    print("acceso_denegado")
if contraseña_almacenada != contraseña_ingresada:
    acceso_permitido == False
    print("acceso denegado")
if acceso_permitido == False:
    print("acceso denegado")

print("gracias por usar el sistema seguro del banco")