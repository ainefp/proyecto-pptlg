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
    - A lo largo del juego puede responder con palabras clave a cualquier pregunta en el momento en que la terminal le permita escribir. Dichas palabras son las siguientes:
    - Cuando quiera salir del juego puede escribir 'a', 'abandonar' o 'salir'.
    - Si desea ver a qué número corresponde cada arma a lo largo de las partidas, puede escribir 'menue'.
    - También puede acceder a este menú escribiendo 'menui', 'ayuda' o 'help'.
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

def opcion_ayuda(respuesta: str) -> bool:
    '''
    Comprueba si la palabra que se le pasa es una palabra clave.

    Parámetros
    respuesta
        Palabra que introduce el usuario

    Devuelve
    bool
        True si la palabra corresponde a alguna acción, False en caso contrario.
    '''
    match respuesta:
        case "a" | "abandonar" | "salir" | "menui" | "ayuda" | "help" | "menue" | "reglas":
            return True
        case _:
            return False

def opcion_usuario_partida(respuesta: str) -> bool:
    '''
    Comprueba si el número que se le pasa se encuentra en el intervalo entre 0 y 4 incluídos.
    Utilizamos esta función porque pedimos el número como str y no como int para permitir que el usuario escriba palabras clave.

    Parámetros
    respuesta
        Número que introduce el usuario

    Devuelve
    bool
        True si el número se encuentra entre 0 y 4, False en caso contrario.
    '''
    return respuesta in ["1", "2", "3", "4", "5"]

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

Finalizado = False

print("Bienvenid@ al juego, a continuación mostraremos el menú de inicio seguido del menú de elecciones.")

menu_inicial()
menu_eleccion()

respuesta = ""
respuesta_valida = False

while not respuesta_valida:
    respuesta = input("\n¿Quiere ver las reglas del juego? [s/n] ")

    if respuesta != "s" and respuesta != "n" and not opcion_ayuda(respuesta):
        print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's', 'n' o alguna palabra clave.\n")

    match respuesta:
        case "s" | "reglas":
            print()
            reglas()
            respuesta_valida = True
        case "n":
            respuesta_valida = True
        case "a" | "abandonar" | "salir":
            respuesta_valida = True
            Finalizado = True
        case "menui" | "ayuda" | "help":
            menu_inicial()
        case "menue":
            menu_eleccion()

sleep(0.2)

while not Finalizado:
    victorias_usuario = 0
    victorias_ordenador = 0

    sleep(0.1)
    print("_____________________________________________________________\n")
    sleep(0.1)

    while victorias_ordenador < 3 and victorias_usuario < 3:
        pregunta_usuario = input("Elija una de las opciones: ")

        while not opcion_usuario_partida(pregunta_usuario) and not opcion_ayuda(pregunta_usuario):
            print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 3, por favor inténtelo de nuevo.\n")
            pregunta_usuario = input("Elija una de las opciones: ")
        
        if opcion_usuario_partida(pregunta_usuario):
            opcion_usuario = int(pregunta_usuario) - 1
        else:
            match pregunta_usuario:
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

        sleep(0.3)

        print("Tu elección ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), "\n")

        sleep(0.6)

        resultado = partida(opcion_ordenador, opcion_usuario)

        if resultado:
            victorias_ordenador += 1
            print("El ordenador ha ganado esta partida.")
            sleep(0.1)
            print("\nRecuento de puntos:")
            sleep(0.1)
            print("Victorias usuario:", victorias_usuario, " |  Victorias ordenador:", victorias_ordenador)
        elif not resultado:
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

    repeticion = ""
    repeticion_valida = False

    while not repeticion_valida:
        repeticion = input("\n¿Quiere volver a jugar o desea salir? s(seguir) / a(abandonar): ")

        if repeticion != "s" and not opcion_ayuda(repeticion):
            print("El parámetro introducido no es válido, por favor inténtelo de nuevo respondiendo con 's' para seguir jugando, 'a' para abandonar o una palabra clave.\n")

        match repeticion:
            case "s":
                repeticion_valida = True
                sleep(0.4)
                print("_____________________________________________________________")
            case "a" | "abandonar" | "salir":
                repeticion_valida = True
                Finalizado = True
            case "reglas":
                print()
                reglas()
            case "menui" | "ayuda" | "help":
                menu_inicial()
            case "menue":
                menu_eleccion()
    
sleep(0.5)
print("\nEspero que se haya divertido, hasta la próxima.")

# Queda por implementar la llamada a funciones durante la partida.
# Preguntar si puedo mejorar los whiles.
# Implementar lo del ordenador tramposo.