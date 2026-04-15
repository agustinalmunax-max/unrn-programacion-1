nombre = "Lautaro"
def mostrar_saludo():
    print("¡Hola! ¡Esta funcion solo muestra este texto!")
def devolver_saludo():
    return "¡Hola! ¡te devuelvo el saludo!"
def saludo_personalizado():
    return f"¡Hola {nombre}! ¡Que bueno verte por acá¡"

mostrar_saludo()
print(devolver_saludo())
print(saludo_personalizado())