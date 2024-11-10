from random import randint
from time import sleep

def num_aleatorio() -> int:
    '''
    Genera y devuelve un número aleatorio entre 0 y 4 (ambos incluídos)

    Parámetros
    No recibe nada

    Devuelve
    int
        Número aleatorio entre 0 y 4
    '''
    return randint(0, 4)

def menu_inicial() -> str:
    '''
    Genera un menú de presentación antes de comenzar el juego.

    Parámetros
    No recibe nada

    Devuelve
    str
        Menú inicial del juego
    '''
    print("""
    - Cuando quiera salir del juego puede responder 'a', 'abandonar' o 'salir' a cualquier pregunta en el momento en que la terminal le permita escribir.
    - Si desea ver a qué número corresponde cada arma a lo largo de las partidas, puede responder 'menue' a cualquier pregunta en el momento en que la terminal le permita escribir.
    - También puede acceder a este menú respondiendo 'menui', 'ayuda' o 'help' a cualquier pregunta en el momento en que la terminal le permita escribir si lo desea.
    - Para continuar jugando presione 's' cuando se le indique.
    """, end="")
    sleep(0.1)

def menu_eleccion() -> str:
    '''
    Muestra el menú de elecciones, el usuario lo utiliza para ver a qué arma corresponde cada número.

    Parámetros
    No recibe nada

    Devuelve
    str
        Menú de elección de arma
    '''
    print("""
    1. Piedra
    2. Spock
    3. Papel
    4. Lagarto
    5. Tijeras
    """)
    sleep(0.1)

def reglas() -> str:
    '''
    Pregunta al usuario si quiere conocer las reglas del juego para mostrar, o no, más información.
    
    Parámetros
    No recibe nada

    Devuelve
    str
        Si 'respuesta' es 's' imprime las reglas del juego
        Si 'respuesta' es 'n' no imprime nada
        Si 'respuesta' es cualquier otra cosa, imprime un mensaje de error y pregunta de nuevo
    '''
    print("Partiendo del juego básico (Piedra, Papel y Tijeras) llevamos a cabo esta expansión, en honor a Sheldon Cooper, que incluye Lagarto y Spock.")
    sleep(0.1)
    print("Las reglas son sencillas, el objetivo del juego es vencer al oponente con el arma seleccionada. Cada arma gana a dos armas y a su vez pierde contra dos armas.")
    sleep(0.1)
    print("Entiéndase por 'arma' cada una de las opciones mostradas en el menú inicial.\n")
    sleep(0.3)
    print("Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto, el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto, el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.\n")
    sleep(0.1)
    print("Para que se vea de forma más clara:\n")
    sleep(0.2)
    print("     Piedra > Tijeras y Lagarto")
    sleep(0.1)
    print("     Tijeras > Lagarto y Papel")
    sleep(0.1)
    print("     Lagarto > Papel y Spock")
    sleep(0.1)
    print("     Papel > Spock y Piedra")
    sleep(0.1)
    print("     Spock > Piedra y Tijeras")
    sleep(0.5)

def eleccion(numero: int) -> str:
    '''
    Transforma el número que se le indique en uno de los nombres de las jugadas. Recibe por número tanto la elección del usuario como la del ordenador.
    Esta función no tiene mayor relevancia para el desempeño del código, su utilidad es favorecer a la claridad de los usuarios.

    Parámetros
    numero: int
        Número a transformar

    Devuelve
    str
        Nombre del arma seleccionada
    '''
    match numero:
        case 0:
            return "piedra"
        case 1:
            return "spock"
        case 2:
            return "papel"
        case 3:
            return "lagarto"
        case 4:
            return "tijeras"

def partida(ordenador: int, usuario: int) -> bool | str:
    '''
    Ejecución de la partida. Recibe en primer lugar el número del arma seleccionada por el ordenador, seguido de la selección del usuario.

    Parámetros
    ordenador: int
        Selección del ordenador
    usuario: int
        Selección del usuario

    Devuelve
    str
        Cuando el resultado de la partida es "empate"
    bool
        True si gana el ordenador, False si gana el usuario
    '''
    if ordenador == usuario:
        return "empate"
    elif ordenador == (usuario + 1) % 5 or ordenador == (usuario + 2) % 5: # Con estas fórmulas gana el ordenador
        return True
    return False

Finalizar = False
repeticion = "s"

print("Bienvenid@ al juego, a continuación mostraremos el menú de inicio seguido del menú de elecciones.")

menu_inicial()
menu_eleccion()

respuesta = input("¿Quiere ver las reglas del juego? (s/n) ")

while respuesta != "s" and respuesta != "n" and respuesta != "a" and respuesta != "abandonar" and respuesta != "salir" and respuesta != "menui" and respuesta != "ayuda" and respuesta != "help" and respuesta != "menue":
    sleep(0.1)
    print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' o 'n'.\n")
    respuesta = input("¿Quiere ver las reglas del juego? (s/n) ")
else:
    match respuesta:
        case "a":
            repeticion = "n"
        case "abandonar":
            repeticion = "n"
        case "salir":
            repeticion = "n"
        case "menui":
            menu_inicial()
            respuesta = input("\n¿Quiere ver las reglas del juego? (s/n) ")
        case "ayuda":
            menu_inicial()
            respuesta = input("\n¿Quiere ver las reglas del juego? (s/n) ")
        case "help":
            menu_inicial()
            respuesta = input("\n¿Quiere ver las reglas del juego? (s/n) ")
        case "menue":
            menu_eleccion()
            respuesta = input("¿Quiere ver las reglas del juego? (s/n) ")

    if respuesta == "s":
        print()
        reglas()

sleep(0.2)

while repeticion == "s" and not Finalizar:
    victorias_usuario = 0
    victorias_ordenador = 0

    sleep(0.1)
    print("_____________________________________________________________\n")
    sleep(0.1)

    while victorias_ordenador < 3 and victorias_usuario < 3:
        opcion_usuario = int(input("Elija una de las opciones: ")) - 1

        while opcion_usuario < 0 or opcion_usuario > 4:
            print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 3, por favor inténtelo de nuevo.\n")
            opcion_usuario = int(input("Elija una de las opciones: ")) - 1

        opcion_ordenador = num_aleatorio()

        sleep(0.3)
        print("Tu elección ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), "\n")

        sleep(1)

        resultado = partida(opcion_ordenador, opcion_usuario)

        if resultado == True:
            victorias_ordenador += 1
            print("El ordenador ha ganado esta partida.")
            sleep(0.1)
            print("\nRecuento de puntos:")
            sleep(0.1)
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        elif resultado == False:
            victorias_usuario += 1
            print("Tú has ganado esta partida.")
            sleep(0.1)
            print("\nRecuento de puntos:")
            sleep(0.1)
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        elif resultado == "empate":
            print("El resultado de esta partida ha sido", resultado)
            sleep(0.1)
            print("\nRecuento de puntos:")
            sleep(0.1)
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        
        sleep(0.4)

        print("_____________________________________________________________\n")

        sleep(0.8)

    if victorias_usuario > victorias_ordenador:
        print("Felicidades!! Has ganado las tres partidas, puedes seguir jugando si lo deseas.\n\n")
    else:
        print("Vaya, el ordenador ha ganado las tres partidas, te deseo más suerte la próxima vez.\n\n")
    

    sleep(0.5)
    repeticion = input("¿Quiere volver a jugar o desea salir? s(seguir) / a(abandonar) ")

    while repeticion != "s" and repeticion != "a" and repeticion != "abandonar" and repeticion != "salir" and repeticion != "menui" and repeticion != "ayuda" and repeticion != "help" and repeticion != "menue":
        sleep(0.1)
        print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' para seguir jugando o 'a' para abandonar.\n")
        repeticion = input("¿Quiere volver a jugar o desea salir? s(seguir) / a(abandonar) ")
    else:
        match repeticion:
            case "s":
                sleep(0.4)
                print("_____________________________________________________________")
            case "a":
                Finalizar = True
            case "abandonar":
                Finalizar = True
            case "salir":
                Finalizar = True
            case "menui":
                menu_inicial()
            case "ayuda":
                menu_inicial()
            case "help":
                menu_inicial()
            case "menue":
                menu_eleccion()

sleep(0.5)
print("\nEspero que se haya divertido, hasta la próxima.")