for time import sleep

def paso_a_paso(texto: str) -> str:
    for letra in range(texto):
        print(letra)
        sleep(0.1)

        sleep(0.1)
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