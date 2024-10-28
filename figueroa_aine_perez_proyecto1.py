def num_aleatorio():
    import random
    print(random.randint(0, 3))

def menu():
    print("Bienvenid@ al juego, a continuación mostraremos una breve explicación del funcionamiento y el menú de opciones.")
    print("Piedra gana a tijera; tijera gana a papel; papel gana a piedra.")
    # print("Piedra gana a tijera y a lagarto; tijera gana a papel y a lagarto; papel gana a piedra y a spock; lagarto gana a spock y a papel; spock gana a tijeras y a piedra.")
    print("""
    1. Piedra   // gana a tijera
    2. Papel    // gana a piedra
    3. Tijera   // gana a papel
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

def partida(ordenador, usuario):
    victorias_usuario = 0
    victorias_ordenador = 0

    while victorias_ordenador < 3 or victorias_usuario < 3:
        if ordenador == usuario:
            pass
        if ordenador == 1:
            if usuario == 3:
                victorias_ordenador += 1
            if usuario == 2:
                victorias_usuario += 1
        if ordenador == 2:
            if usuario == 1:
                victorias_ordenador += 1
            if usuario == 3:
                victorias_usuario += 1
        if ordenador == 3:
            if usuario == 2:
                victorias_ordenador += 1
            if usuario == 1:
                victorias_usuario += 1


menu()

opcion_usuario = int(input("Elija una de las opciones: "))

while opcion_usuario < 1 or opcion_usuario > 3:
    print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 5, por favor inténtelo de nuevo.")
    opcion_usuario = int(input("Elija una de las opciones: "))

partida(num_aleatorio, opcion_usuario)