numero = int(input("Introduce un numero: "))

if numero > 10:
    print("El numero es mayor que 10")
elif numero < 10:
    print("El numero es menor que 10")
else:
    print("El numero es igual que 10")

if numero %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")