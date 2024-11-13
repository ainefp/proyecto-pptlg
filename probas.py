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


    >>> partida(0, 0)
    "empate"

    >>> partida(1, 1)
    "empate"

    >>> partida(2, 2)
    "empate"

    >>> partida(3, 3)
    "empate"

    >>> partida(4, 4)
    "empate"

    >>> partida(0, 1)
    False

    >>> partida(0, 2)
    False

    >>> partida(0, 3)
    True

    >>> partida(0, 4)
    True

    >>> partida(1, 0)
    True

    >>> partida(1, 2)
    False

    >>> partida(1, 3)
    False

    >>> partida(1, 4)
    True

    >>> partida(2, 0)
    True

    >>> partida(2, 1)
    True

    >>> partida(2, 3)
    False

    >>> partida(2, 4)
    False

    >>> partida(3, 0)
    False

    >>> partida(3, 1)
    True

    >>> partida(3, 2)
    True

    >>> partida(3, 4)
    False

    >>> partida(4, 0)
    False

    >>> partida(4, 1)
    False

    >>> partida(4, 2)
    True

    >>> partida(4, 3)
    True
    '''
    
    if ordenador == usuario:
        return "empate"
    elif ordenador == (usuario + 1) % 5 or ordenador == (usuario + 2) % 5: # Con estas fórmulas gana el ordenador
        return True
    return False

# COMANDO PARA REALIZAR PRUEBAS:
#       python3 -m doctest -v probas.py

# Al realizar las pruebas da 5 errores, la palabra "empate" falla 5 veces, pero los resultados son correctos.