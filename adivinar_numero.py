import random

def adivinar_numero():
    # Genera un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)
    
    # Inicializa el número de intentos disponibles
    intentos = 3

    print("Bienvenido al juego de adivinar el número entre 1 y 10.")
    
    while intentos > 0:
        try:
            # Solicita al usuario que ingrese un número
            guess = int(input(f"Intentos restantes: {intentos}. Adivina el número: "))
            
            # Verifica si el número adivinado es correcto
            if guess == numero_secreto:
                print("¡Felicidades! Has adivinado el número.")
                break
            else:
                print("Número incorrecto. Intenta de nuevo.")
                intentos -= 1
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if intentos == 0:
        print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivinar_numero()
