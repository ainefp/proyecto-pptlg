def num_aleatorio():
    import random
    print(random.randint(0, 5))

def menu():
    print("Bienvenid@ al juego, a continuación mostraremos una breve explicación del funcionamiento y el menú de opciones.")
    print("Piedra gana a tijera; tijera gana a papel; papel gana a piedra.")
    # print("Piedra gana a tijera y a lagarto; tijera gana a papel y a lagarto; papel gana a piedra y a spock; lagarto gana a spock y a papel; spock gana a tijeras y a piedra.")
    print("""
    1. Piedra
    2. Papel
    3. Tijera
    """)
        #   4. Lagarto
        #   5. Spock
        #   """)

menu()

opcion_usuario = int(input("Elija una de las opciones: "))

while opcion_usuario < 1 or opcion_usuario > 5:
    print("El parámetro introducido no es válido, debe introducir un número entero comprendido entre 1 y 5, por favor inténtelo de nuevo.")
    opcion_usuario = int(input("Elija una de las opciones: "))
