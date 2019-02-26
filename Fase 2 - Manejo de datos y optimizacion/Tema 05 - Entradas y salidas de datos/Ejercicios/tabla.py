#!/usr/bin/env python3
# coding: utf-8

class ArgumentError(Exception):
    def __init__(self, name, value, msg=None):
        if msg is None:
            msg = (f"Error: argumento {arg_name} con valor {arg_value} es "
                    "incorrecto.")
        self.value = value
        self.name = name


def imprimir_ayuda(programa):
    print(( "Uso del programa:\n"
           f"{programa} [-h] <filas> <columnas>\n\n"
            "Argumentos:\n"
            "filas: número de filas.\n"
            "columnas: número de columnas.\n\n"
            "Opciones:\n"
            "-h: Mostrar la ayuda.\n\n"))

import re
import collections.abc

def parse_parametros(params):
    """
    Extrae las opciones y argumentos introducidos para un comando.
    Argumentos:
        params: Parámetros del comando. Puede ser una cadena con todos los
            parámetros o una secuencia de parámetros.

    Retorno:
        Devuelve un diccionario con los siguientes valores:
            - "opciones": conjunto con las opciones extraídas como cadenas.
            - "argumentos": lista con los argumentos introducidos en orden. Los
            argumentos son del mismo tipo de dato a como se pasaron inicialmente.

    Excepciones:
        ArgumentError: Si los parámetros pasados por argumento no son una cadena
            de caracteres ni una sequencia.
    """
    # Si los parámetros están en una cadena se convierte a una secuencia.
    if isinstance(params, str):
        pass #params = re.split("[^"][ \t]+", params)
    elif not isinstance(params, collections.abc.Sequence):
        raise ArgumentError("params", params,
                            "Los parámetros no son una secuencia ni una cadena "
                            "de caracteres.")

    params_dict= {"opciones": set(), "argumentos": []}

    # Procesa las opciones
    for param in params:
        if isinstance(param, str):
            param = param.strip()
            if param.startswith('-'):
                params_dict["opciones"].update(param[1:])
                continue
        params_dict["argumentos"].append(param)

    return params_dict



import sys

if len(sys.argv) == 1:
    imprimir_ayuda(sys.argv[0])
    sys.exit()

params = parse_parametros(sys.argv[1:])

# Comprueba las opciones
for opcion in params["opciones"]:
    if opcion == 'h':
        imprimir_ayuda(sys.argv[0])
        sys.exit()
    # elif Otras opciones
    else:
        print(f"\nLa opción -{opcion} es incorrecta.")
        imprimir_ayuda(sys.argv[0])
        sys.exit()

# Comprueba número de argumentos
if len(params["argumentos"]) != 2:
    print("\nHas introducido un número incorrecto de argumentos\n")
    imprimir_ayuda(sys.argv[0])
    sys.exit()

# Obtiene número de filas y columnas
valores = {"filas": None, "columnas": None}
for i, nombre_arg in enumerate(("filas", "columnas")):
    try:
        valores[nombre_arg] = int(params["argumentos"][i])
    except ValueError:
        print(f"Error: el número de {nombre_arg} debe ser un entero.\n")
        imprimir_ayuda(sys.argv[0])
        sys.exit()

    if not 0<=valores[nombre_arg]<=9:
        print(f"Error: el número de {nombre_arg} debe estar entre 0 y 9.\n")
        imprimir_ayuda(sys.argv[0])
        sys.exit()

# Realiza el comando
for _ in range(valores["filas"]):
    print(' * '*valores["columnas"])

