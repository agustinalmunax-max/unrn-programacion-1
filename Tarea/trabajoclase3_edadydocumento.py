edad_ingresada = int(input("edad:"))
edad_minima = 18

if edad_ingresada >= edad_minima:
    documento = input("¿tiene DNI? (SI/NO): ")
    if documento == "SI":
        numero_dni = input("Ingrese numero de DNI: ")
        if len(numero_dni) == 8:
            print("Acceso permitido")
        else:
            print("Acceso denegado: DNI falso detectado")
    else:
        print("Acceso denegado: No tiene documentacion")
else:
    print("Acceso denegado: Menor de edad")

input()



