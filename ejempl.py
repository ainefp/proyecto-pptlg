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
    print("Las reglas son sencillas, el objetivo del juego es vencer al oponente con el arma seleccionada. Cada arma gana a dos armas y a su vez pierde contra dos armas.")
    print("Entiéndase por 'arma' cada una de las opciones mostradas en el menú inicial.\n")
    print("Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto, el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto, el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.\n")
    print("Para que se vea de forma más clara:\n")
    print("     Piedra > Tijeras y Lagarto")
    print("     Tijeras > Lagarto y Papel")
    print("     Lagarto > Papel y Spock")
    print("     Papel > Spock y Piedra")
    print("     Spock > Piedra y Tijeras")

def opcion_ayuda(respuesta: str) -> bool:
    '''
    Comprueba

    Parámetros
    respuesta
        fdnf

    Devuelve
    bool
        True blabla
    '''
    match respuesta:
        case "a" | "abandonar" | "salir" | "menui" | "ayuda" | "help" | "menue" | "reglas":
            return True
        case _:
            return False

def opcion_usuario_partida(respuesta: str) -> bool:
    '''
    Comprueba

    Parámetros
    respuesta
        fdnf

    Devuelve
    bool
        True blabla
    '''
    match respuesta:
        case "0" | "1" | "2" | "3" | "4":
            return True
        case _:
            return False

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

print("Bienvenid@ al juego, a continuación mostraremos el menú de inicio seguido del menú de elecciones.")

menu_inicial()
menu_eleccion()

respuesta = ""
respuesta_valida = False

while respuesta_valida == False:
    respuesta = input("\n¿Quiere ver las reglas del juego? [s/n] ")

    if respuesta != "s" and respuesta != "n" and opcion_ayuda(respuesta) == False:
        print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' o 'n'.\n")

    match respuesta:
        case "s" | "reglas":
            print()
            reglas()
            respuesta_valida = True
        case "n":
            respuesta_valida = True
        case "a" | "abandonar" | "salir":
            Finalizar = True
        case "menui" | "ayuda" | "help":
            menu_inicial()
            respuesta = ""
        case "menue":
            menu_eleccion()
            respuesta = ""

while not Finalizar:
    victorias_usuario = 0
    victorias_ordenador = 0

    print("_____________________________________________________________\n")

    while victorias_ordenador < 3 and victorias_usuario < 3:
        pregunta_usuario = input("Elija una de las opciones: ")

        while opcion_usuario_partida(pregunta_usuario) and opcion_ayuda(pregunta_usuario) == False:
            print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 3, por favor inténtelo de nuevo.\n")
            pregunta_usuario = input("Elija una de las opciones: ")
        
        match pregunta_usuario:
            case "0" | "1" | "2" | "3" | "4":
                opcion_usuario = int(pregunta_usuario) - 1
            case "reglas":
                print()
                reglas()
            case "a" | "abandonar" | "salir":
                break
            case "menui" | "ayuda" | "help":
                menu_inicial()
                opcion_usuario = input(int("Elija una de las opciones: " - 1))
            case "menue":
                menu_eleccion()
                opcion_usuario = input(int("Elija una de las opciones: " - 1))

        opcion_ordenador = num_aleatorio()


        print("Tu elección ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), "\n")

        sleep(0.6)

        resultado = partida(opcion_ordenador, opcion_usuario)

        if resultado == True:
            victorias_ordenador += 1
            print("El ordenador ha ganado esta partida.")
    
            print("\nRecuento de puntos:")
    
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        elif resultado == False:
            victorias_usuario += 1
            print("Tú has ganado esta partida.")
    
            print("\nRecuento de puntos:")
    
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        elif resultado == "empate":
            print("El resultado de esta partida ha sido", resultado)
    
            print("\nRecuento de puntos:")
    
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        
        sleep(0.4)

        print("_____________________________________________________________\n")

        sleep(0.8)

    if victorias_usuario > victorias_ordenador:
        print("Felicidades!! Has ganado las tres partidas, puedes seguir jugando si lo deseas.\n\n")
    else:
        print("Vaya, el ordenador ha ganado las tres partidas, te deseo más suerte la próxima vez.\n\n")
    


    repeticion = ""
    repeticion_valida = False

    while repeticion_valida == False:
        repeticion = input("\n¿Quiere volver a jugar o desea salir? s(seguir) / a(abandonar) ")

        if repeticion != "s" and opcion_ayuda(repeticion) == False:
            print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' para seguir jugando o 'a' para abandonar.\n")

        match repeticion:
            case "s":
                sleep(0.4)
                print("_____________________________________________________________")
            case "reglas":
                print()
                reglas()
                repeticion = input("\n¿Quiere volver a jugar o desea salir? s(seguir) / a(abandonar) ")
            case "a" | "abandonar" | "salir":
                Finalizar = True
            case "menui" | "ayuda" | "help":
                menu_inicial()
                repeticion = ""
            case "menue":
                menu_eleccion()
                repeticion = ""

print("\nEspero que se haya divertido, hasta la próxima.")

# Queda por implementar la llamada a funciones durante la partida.
# Preguntar si puedo mejorar los whiles.
# Implementar lo del ordenador tramposo.