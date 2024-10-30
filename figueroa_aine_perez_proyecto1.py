def num_aleatorio() -> int:
    import random
    return random.randint(0, 2)

def menu() -> str:
    print("Bienvenid@ al juego, a continuación mostraremos una breve explicación del funcionamiento y el menú de opciones.")
    print("Piedra gana a tijera; tijera gana a papel; papel gana a piedra.")
    # print("Piedra gana a tijera y a lagarto; tijera gana a papel y a lagarto; papel gana a piedra y a spock; lagarto gana a spock y a papel; spock gana a tijeras y a piedra.")
    print("""
    0. Piedra   // gana a tijera
    1. Papel    // gana a piedra
    2. Tijeras   // gana a papel
    """)
    # 1 > 3 // gana ordenador
    # 1 < 2

    # 2 > 1 // gana ordenador
    # 2 < 3

    # 3 > 2 // gana ordenador
    # 3 < 1

        #   4. Lagarto
        #   5. Spock
        #   """)

def eleccion(numero: int) -> str:
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
    elif ordenador == (usuario +1) % 3:
        return True
    return False

victorias_usuario = 0
victorias_ordenador = 0

menu()

while victorias_ordenador < 3 and victorias_usuario < 3:
    opcion_usuario = int(input("Elija una de las opciones: "))

    while opcion_usuario < 0 or opcion_usuario > 2:
        print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 0 y 2, por favor inténtelo de nuevo.")
        opcion_usuario = int(input("Elija una de las opciones: "))

    opcion_ordenador = num_aleatorio()

    print("Tu eleccion ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), num_aleatorio())

    resultado = partida(opcion_ordenador, opcion_usuario)

    if resultado == True:
        victorias_ordenador += 1
        print("El ordenador ha ganado esta partida \n")
    elif resultado == False:
        victorias_usuario += 1
        print("Tú has ganado esta partida \n")
    elif resultado == "empate":
        print("El resultado de esta partida ha sido", resultado, "\n")

if victorias_usuario > victorias_ordenador:
    print("Felicidades!! Has ganado las tres partidas, puedes seguir jugando si lo deseas.")
else:
    print("Vaya, el ordenador ha ganado las tres partidas, te deseo más suerte la próxima vez.")