def calcular_edad():
    # Solicita al usuario que ingrese su año de nacimiento
    try:
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    except ValueError:
        print("Por favor, ingrese un año válido.")
        return

    # Obtiene el año actual (puedes usar la biblioteca datetime para esto)
    from datetime import datetime
    año_actual = datetime.now().year

    # Calcula la edad del usuario
    edad = año_actual - año_nacimiento

    # Muestra la edad calculada
    print(f"Su edad es aproximadamente {edad} años.")

if __name__ == "__main__":
    calcular_edad()
