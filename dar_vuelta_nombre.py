def dar_vuelta_nombre():
    # Solicita al usuario que ingrese su nombre
    nombre = input("Ingrese su nombre: ")

    # Invierte el nombre
    nombre_invertido = nombre[::-1]

    # Muestra el nombre invertido
    print(f"Su nombre al revés es: {nombre_invertido}")

if __name__ == "__main__":
    dar_vuelta_nombre()
