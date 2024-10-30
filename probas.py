def num_aleatorio():
    import random
    return random.randint(0, 2)

def eleccion(numero):
    match numero:
        case 0:
            return "piedra"
        case 1:
            return "papel"
        case 2:
            return "tijeras"

usuario = int(input("pon un número (0-2):  "))
print("menú:")
print("""
      0. papel
      1. pedra
      2. tijeras
      """)

print("El usuario escoge", eleccion(usuario), usuario, "y el ordenador", eleccion(num_aleatorio()), num_aleatorio())