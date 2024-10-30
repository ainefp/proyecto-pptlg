def num_aleatorio():
    import random
    return int(random.randint(0, 3))

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

def eleccion(numero):
    match numero:
        case 1:
            return "piedra"
        case 2:
            return "papel"
        case 3:
            return "tijeras"
    
        # case 3:
        #     return "lagarto"
        # case 4:
        #     return "spock"

def partida(ordenador, usuario):
    if ordenador == usuario:
        return "empate"
    elif ordenador == (usuario +1) % 3:
        return True
    return False

# victorias_usuario = 0
# victorias_ordenador = 0
opcion_ordenador = num_aleatorio()

menu()


#while victorias_ordenador < 3 or victorias_usuario < 3:

opcion_usuario = int(input("Elija una de las opciones: "))

resultado = partida(opcion_ordenador, opcion_usuario)

while opcion_usuario < 1 or opcion_usuario > 3:
    print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 3, por favor inténtelo de nuevo.")
    opcion_usuario = int(input("Elija una de las opciones: "))

print("Tu eleccion ha sido", eleccion(opcion_usuario), "y la del ordenador", eleccion(opcion_ordenador), num_aleatorio())

if resultado == True:
    #victorias_ordenador += 1
    print("El ordenador ha ganado esta partida")
elif resultado == False:
    #victorias_usuario += 1
    print("Tú has ganado esta partida")
elif resultado == "empate":
    print(resultado)
    #print("El resultado de esta partida ha sido", partida(opcion_ordenador, opcion_usuario))


# if victorias_usuario > victorias_ordenador:
#     print("Felicidades!! Has ganado las tres partidas, puedes seguir jugando si lo deseas.")
# elif victorias_usuario == victorias_ordenador:
#     print("Habéis empatado las tres partidas, puedes seguir jugando para desempatar.")
# else:
#     print("Vaya, el ordenador ha ganado las tres partidas, te deseo más suerte la próxima vez.")