"""
Created on Sun Mar 12 15:11:18 2023

@author: DELACRUZ JUNIOR RAUL

APLICACION CLIENTE
"""


import socket
import time
import json
import random
import re


# Crear un socket y conectar con el servidor
server_address = input("Introduce la dirección del servidor: ")
server_port = int(input("Introduce el puerto del servidor: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_address, server_port))
#sock.connect(("127.0.0.1", 1024))

respuesta = sock.recv(1024).decode('utf-8')
print("\n")
print(respuesta)
print("\n")
start_time = time.time()

# Elegir la dificultad del juego
#print("Selecciona la dificultad:")
#print("1. Principiante (9x9 casillas, 10 minas)")
#print("2. Avanzado (16x16 casillas, 40 minas)")

opcion = int(input("Elige una opción: "))

# convert num to str, then encode to utf8 byte
sock.send(bytes(str(opcion), 'utf8'))


# Jugar mientras no se haya ganado o perdido
while True:


    #Actualizar el tablero
    tablero = sock.recv(2048).decode()
    board_data = json.loads(tablero)

    #print(board_data)

    for i in range(board_data['dim_size']):
        if i == 0:
            print("   ", end="")
            for j in range(board_data['dim_size']):
                print(f"{j}  ", end="")
            print("\n-------------------------------")
        print(f"{i} ", end="")
        for j in range(board_data['dim_size']):
            if [i, j] in board_data['dug']:
                print(f"|{board_data['board'][i][j]} ", end="")
            else:
                print("|  ", end="")
        print("|")

    #MANDAMOS LAS COORDENADAS
    print("Ingresa tu coordenada: ")
    user_input = input()
    sock.send(user_input.encode('utf-8'))


    respuesta = sock.recv(1024).decode('utf-8')
    #Comprobar si se ha ganado o perdido
    print(respuesta)

    if respuesta == "PERDEDOR":
        print("¡Has perdido!")
        # Registrar el tiempo de fin de la conexión
        end_time = time.time()
        # Calcular el tiempo total que ha durado la conexión
        total_time = end_time - start_time
        # Imprimir el tiempo total
        print("La conexión ha durado:", total_time, "segundos")
        break
    elif respuesta == "GANADOR":
        print("¡Has ganado!")
        # Registrar el tiempo de fin de la conexión
        end_time = time.time()
        # Calcular el tiempo total que ha durado la conexión
        total_time = end_time - start_time
        # Imprimir el tiempo total
        print("La conexión ha durado:", total_time, "segundos")
        break


# Cerrar el socket
sock.close()
#65432