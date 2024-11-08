from random import randint
from time import sleep

def num_aleatorio() -> int:
    '''
    Genera y devuelve un número aleatorio entre 0 y 2 (ambos incluídos)
    '''
    return randint(0, 2)

def menu() -> str:
    '''
    Función que genera un menú de presentación antes de comenzar el juego.
    Pregunta al usuario si quiere conocer las reglas para mostrar más información
    '''
    print("Bienvenid@ al juego, a continuación mostraremos el menú de inicio.")
    print("""
    1. Piedra
    2. Papel
    3. Tijeras
    4. Lagarto
    5. Spock
    """)

    # para lagart-spock usamos %5 porque cada 1 gana a los 2 siguientes

def reglas() -> str:
    '''
    Reglas del juego.
    '''
    respuesta = input("¿Quiere ver las reglas del juego? (s/n) ")
    while respuesta != "s" and respuesta != "n":
        print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' o 'n'.\n")
        respuesta = input("¿Quiere ver las reglas del juego? (s/n) ")
    
    print()
    if respuesta == "s":
        print("Partiendo del juego básico (Piedra, Papel y Tijeras), llevamos a cabo esta expansión, en honor a Sheldon Cooper, que incluye Lagarto y Spock.")
        print("Las reglas son sencillas, el objetivo del juego es vencer al oponente con el arma seleccionada. Cada arma gana a dos armas y a su vez pierde contra dos armas.")
        print("Entiéndase por 'arma' cada una de las opciones mostradas en el menú inicial.\n")
        print("Piedra gana a tijera y a lagarto; tijera gana a papel y a lagarto; papel gana a piedra y a spock; lagarto gana a spock y a papel; spock gana a tijeras y a piedra.")
        print("bla bla bla\n")

def eleccion(numero: int) -> str:
    '''
    Transforma el número que se le indique en uno de los nombres de las jugadas.
    Esta función no tiene mayor relevancia para el desempeño del código, su utilidad es favorecer a la claridad de los usuarios.
    '''
    match numero:
        case 0:
            return "piedra"
        case 1:
            return "papel"
        case 2:
            return "tijeras"
    
        # case 3:
        #     return "lagarto"
        # case 4:
        #     return "spock"

def partida(ordenador: int, usuario: int) -> bool | str:
    if ordenador == usuario:
        return "empate"
    elif ordenador == (usuario +1) % 3: # Con esta fórmula gana el ordenador
        return True
    return False

victorias_usuario = 0
victorias_ordenador = 0

menu()
reglas()

print("_____________________________________________________________\n")

while victorias_ordenador < 3 and victorias_usuario < 3:
    opcion_usuario = int(input("Elija una de las opciones: ")) - 1

    while opcion_usuario < 0 or opcion_usuario > 2:
        print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 3, por favor inténtelo de nuevo.\n")
        opcion_usuario = int(input("Elija una de las opciones: ")) - 1

    opcion_ordenador = num_aleatorio()

    sleep(0.5)
    print("Tu elección ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), "\n")

    sleep(1)

    resultado = partida(opcion_ordenador, opcion_usuario)

    if resultado == True:
        victorias_ordenador += 1
        print("El ordenador ha ganado esta partida.")
        print("\nRecuento de puntos:\nVictorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
    elif resultado == False:
        victorias_usuario += 1
        print("Tú has ganado esta partida.")
        print("\nRecuento de puntos:\nVictorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
    elif resultado == "empate":
        print("El resultado de esta partida ha sido", resultado)
        print("\nRecuento de puntos:\nVictorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
    
    print("_____________________________________________________________\n")
    sleep(1)

if victorias_usuario > victorias_ordenador:
    print("Felicidades!! Has ganado las tres partidas, puedes seguir jugando si lo deseas.\n")
else:
    print("Vaya, el ordenador ha ganado las tres partidas, te deseo más suerte la próxima vez.\n")