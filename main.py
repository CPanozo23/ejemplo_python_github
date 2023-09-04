# Importa los módulos necesarios
from calcular_edad import calcular_edad
from dar_vuelta_nombre import dar_vuelta_nombre
from adivinar_numero import adivinar_numero

def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("1) Calcular tu edad")
        print("2) Da vuelta tu nombre")
        print("3) Adivina un número en 1 y 10")
        print("0) Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                calcular_edad()
            elif opcion == 2:
                dar_vuelta_nombre()
            elif opcion == 3:
                adivinar_numero()
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()
