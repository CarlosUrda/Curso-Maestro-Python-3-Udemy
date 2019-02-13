#!/usr/bin/env python3
# coding: utf-8

def imprimir_ayuda(programa):
    print(( "Uso del programa:\n"
           f"{programa} [-h] <texto> [<repe>]\n\n"
            "Argumentos:\n"
            "texto: cadena de texto a repetir.\n"
            "repe: número de veces a mostrar la cadena. Por defecto 1.\n\n"
            "Opciones:\n"
            "-h: Mostrar la ayuda."))

import sys

if len(sys.argv) == 1:
    imprimir_ayuda(sys.argv[0])
    quit()

# Procesa las opciones
resto_args = []
for i, argumento in enumerate(sys.argv[1:]):
    if not argumento.startswith('-'):
        resto_args = sys.argv[i+1:]
        break

    for opcion in argumento[1:]:
        if opcion == 'h':
            imprimir_ayuda(sys.argv[0])
            quit()
        # elif Otras opciones
        else:
            print(f"Error: La opción -{opcion} no es correcta\n")
            imprimir_ayuda(sys.argv[0])
            quit()

# Comprueba número de argumentos
len_resto_args = len(resto_args)
if len_resto_args == 0 or len_resto_args > 2:
    print("Has introducido un número incorrecto de argumentos\n")
    imprimir_ayuda(sys.argv[0])
    quit()

# Obtiene número de repeticiones
try:
    repeticiones = int(resto_args[1]) if len_resto_args == 2 else 1
except ValueError:
    print("El número de repeticiones debe ser un entero.\n")

# Realiza el comando
for _ in range(repeticiones):
    print(resto_args[0])

