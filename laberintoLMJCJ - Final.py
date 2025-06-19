from random import randint
from random import shuffle
import time
import os
def animacion():
    print("\n" * 50)
    time.sleep(0.01)
    os.system('cls')                                           #SIRVE EN LA TERMINAL.
    print("                                         ")
    print("█    ██  ███  ███ ███  █ █   █ █████ ████")
    print("█   █  █ █  █ █   █  █ █ ██  █   █   █  █")
    print("█   ████ █ █  ███ ███  █ █ █ █   █   █  █")
    print("█   █  █ █  █ █   █ █  █ █  ██   █   █  █")
    print("███ █  █ ███  ███ █  █ █ █   █   █   ████")
    print()



logo=["                                                    ███             ██            ",
      "                                                    █ █             █ █           ",
      "   █     █ ███ █   ████ ████ █   █ ███            ██  █             █  ██         ",
      "   █     █ █   █   █    █  █ ██ ██ █              █    █ █████████ █    █         ",
      "    █ █ █  ███ █   █    █  █ █ █ █ ███            ███  ██         ██  ███         ",
      "    █ █ █  █   █   █    █  █ █   █ █                 ███           ███            ",
      "     █ █   ███ ███ ████ ████ █   █ ███                █             █             ",
      "                                                     █   ██     ██   █            ",
      "               █████ ████                            █  ██ █   ██ █  █            ",
      "                 █   █  █                            █  ████   ████  █            ",
      "                 █   █  █                            █   ██     ██   █            ",
      "                 █   █  █                            █       █       █            ",
      "                 █   ████                            █      ███      █            ",
      "                                                      █     ███     █             ",
      "█    ██  ███  ███ ███  █ █   █ █████ ████             ███         ███             ",
      "█   █  █ █  █ █   █  █ █ ██  █   █   █  █            █  ██       ██  █            ",
      "█   ████ █ █  ███ ███  █ █ █ █   █   █  █         ███   █ █ █   █ █   ███         ",
      "█   █  █ █  █ █   █ █  █ █  ██   █   █  █         █    █  █ █ █ █  █    █         ",
      "███ █  █ ███  ███ █  █ █ █   █   █   ████         ██  █   ███████   █  ██         ",
      "                                                    █ █             █ █           ",
      "                                                    ███             ███           "
    ]
for linea in logo:
    for c in linea:
        print(c, end='')
        time.sleep(0.001)
    print()
print()
print("¿Que quiere hacer hoy?")
print("1.Jugar")
print("2.¿Como jugar?")
print("3.Finalizar el juego")
input1=input("Ingrese un numero: ")
while input1!='1':
    if input1 == '2':
        print("Controles: ")
        print("a(⬅): El jugador se mueve 2 casillas hacia la izquierda")
        print("w(⬆): El jugador se mueve 2 casillas hacia arriba")
        print("s(⬇): El jugador se mueve 2 casillas hacia abajo")
        print("d(⮕): El jugador se mueve 2 casillas hacia la derecha")
        print()
        print("Reglas:")
        print("No puede atravesar paredes ni salirse del mapa >-<")
        print("Usted empieza fuera del laberinto, antes de entrar a la casilla marcada como 'E'.")
        print("De igual manera, usted tiene que salir del tablero por la casilla marcada como 'S'.")
        print("cada movimiento 'a' 's' 'w' 'd' recorre dos casillas del tablero.")
        print()
        print("Seleccione una de las siguientes opciones: ")
        print("1.Jugar")
        print("2.¿Como jugar?")
        print("3.Finalizar el juego")
        input1 = input("Ingrese un numero: ")
    elif input1=='3':
        print("Nos vemos luego :)")
        break
    else:
        print("Numero incorrecto")
        print("Seleccione una de las siguientes opciones: ")
        print("1.Jugar")
        print("2.¿Como jugar?")
        print("3.Finalizar el juego")
        input1 = input("Ingrese un numero: ")



if input1=='1':
    usuario = input("Ingrese el nombre de usuario: ")
    print()
    print(f"{usuario}, ¿Quieres escoger el tamaño del tablero?")
    print("Tamaño de lado permitido: 2-40 ")
    print()
    print("1.Si")
    print("2.Predeterminado")
    print()
    escoger=input("Ingrese un numero: ")
    while escoger!='1' and escoger!='2':
        print()
        print("Opcion equivocada, elija nuevamente")
        print("1.Si")
        print("2.Predeterminado")
        escoger=input("Ingrese un numero: ")
    if escoger=='2':
        tamano=10
    elif escoger=='1':
        w_list=[f"{i}" for i in range(2, 41)]
        tamanostr =input("Ingrese el tamaño del laberinto que usted desea: ")
        while tamanostr not in w_list:
            print()
            tamanostr=input("Equivocado, marque nuevamente: ")
        if tamanostr in w_list:
            tamano=int(tamanostr)

    matriz_casillas_visitadas = []
    for j in range(tamano):
        l = [0] * tamano
        matriz_casillas_visitadas.append(l)
    x = randint(0, tamano - 1)
    inicio = x
    matriz_casillas_visitadas[x][0] = 1  #matriz para saber que casillas has visitado
    matriz_paredes = []
    for _ in range(tamano):
        l = [{} for _ in range(tamano)]
        matriz_paredes.append(l)
    for i in range(tamano):
        for j in range(tamano):
            direcciones = {"N": 1, "S": 1, "O": 1, "E": 1}
            matriz_paredes[i][j] = direcciones
    matriz_paredes[x][0]["O"] = 0
    y = 0


    def Back_tracking(x: int, y: int):
        matriz_casillas_visitadas[x][y] = 1
        movimientos = [("N", x - 1, y), ("O", x, y - 1), ("S", x + 1, y), ("E", x, y + 1)]
        shuffle(movimientos)
        for i in range(4):
            mov, nx, ny = movimientos[i]
            if nx in range(0, tamano) and ny in range(0,tamano):  # comprobamos si el movimiento pertecenece a la matriz
                if matriz_casillas_visitadas[nx][ny] == 0:
                    if mov == "N":
                        matriz_paredes[x][y]["N"] = 0
                        matriz_paredes[nx][ny]["S"] = 0

                    elif mov == "O":
                        matriz_paredes[x][y]["O"] = 0
                        matriz_paredes[nx][ny]["E"] = 0

                    elif mov == "S":
                        matriz_paredes[x][y]["S"] = 0
                        matriz_paredes[nx][ny]["N"] = 0

                    elif mov == "E":
                        matriz_paredes[x][y]["E"] = 0
                        matriz_paredes[nx][ny]["O"] = 0
                    Back_tracking(nx, ny)
        return None


    Back_tracking(x, y)
    matriz_paredes[tamano - 1][tamano - 1]["S"] = 0
    newtamano = 2 * tamano + 1
    matriz_print = []
    for i in range(newtamano):
        l = ["█"] * (newtamano)
        matriz_print.append(l)
    for z in range(1, newtamano, 2):
        for j in range(newtamano):
            if j % 2 == 1:
                matriz_print[z][j] = " "
            else:
                a = int((z - 1) / 2)
                b = int(j / 2) - 1
                if j == 0:
                    if matriz_paredes[a][0]["O"] == 1:
                        matriz_print[z][j] = "█"
                    else:
                        matriz_print[z][j] = " "
                elif (j > 0):
                    if matriz_paredes[a][b]["E"] == 1:
                        matriz_print[z][j] = "█"
                    else:
                        matriz_print[z][j] = " "
    for z in range(2, newtamano, 2):
        for j in range(newtamano):
            if j % 2 == 1:
                a = int(z / 2) - 1
                b = int((j - 1) / 2)
                if matriz_paredes[a][b]["S"] == 1:
                    matriz_print[z][j] = "█"
                else:
                    matriz_print[z][j] = " "
    matriz_print[2 * inicio + 1][0] = "E"
    matriz_print[newtamano - 1][newtamano - 2] = "S"


    def Imprimir_laberinto(matriz_print: list[list[str]]):
        for i in range(newtamano):
            for j in range(newtamano):
                print(matriz_print[i][j], end="")
            print()


    Imprimir_laberinto(matriz_print)
    # Empezaremos con los movimientos:
    lista = ["a", "w", "s", "d", "salir"]
    flag = True
    casilla_actualx = 2 * inicio + 1
    casilla_actualy = 0
    contador = 0
    while flag:
        mov = input("Ingrese un movimiento: ")
        if mov not in lista:
            print("El movimiento no existe")
        elif mov in lista:
            if contador == 0:
                if mov == "d":
                    casilla_actualy = 1
                    contador += 1
                    matriz_print[casilla_actualx][casilla_actualy] = "P"
                    animacion()
                    Imprimir_laberinto(matriz_print)
                elif mov == "salir":
                    print(f"{usuario}, You lose :(")
                    break
                else:
                    print("Movimiento no valido.")

            else:
                if mov == "a":
                    x1 = casilla_actualx
                    y1 = casilla_actualy - 2
                    if x1 in range(newtamano) and y1 in range(newtamano):
                        if matriz_print[x1][y1] == " " and matriz_print[x1][y1 + 1] == " ":
                            matriz_print[casilla_actualx][casilla_actualy] = " "
                            casilla_actualx = x1
                            casilla_actualy = y1
                            matriz_print[casilla_actualx][casilla_actualy] = "P"
                            contador += 1
                            animacion()
                            Imprimir_laberinto(matriz_print)
                        else:
                            print("Movimiento no valido, existe una pared.")
                    else:
                        print("Movimiento no valido, fuera de rango.")
                elif mov == "w":
                    x1 = casilla_actualx - 2
                    y1 = casilla_actualy
                    if x1 in range(newtamano) and y1 in range(newtamano):
                        if matriz_print[x1 + 1][y1] == " " and matriz_print[x1][y1] == " ":
                            matriz_print[casilla_actualx][casilla_actualy] = " "
                            casilla_actualx = x1
                            casilla_actualy = y1
                            matriz_print[casilla_actualx][casilla_actualy] = "P"
                            contador += 1
                            animacion()
                            Imprimir_laberinto(matriz_print)
                        else:
                            print("Movimiento no valido, existe una pared.")
                    else:
                        print("Movimiento no valido, fuera de rango.")
                elif mov == "d":
                    x1 = casilla_actualx
                    y1 = casilla_actualy + 2
                    if x1 in range(newtamano) and y1 in range(newtamano):
                        if matriz_print[x1][y1] == " " and matriz_print[x1][y1 - 1] == " ":
                            matriz_print[casilla_actualx][casilla_actualy] = " "
                            casilla_actualx = x1
                            casilla_actualy = y1
                            matriz_print[casilla_actualx][casilla_actualy] = "P"
                            contador += 1
                            animacion()
                            Imprimir_laberinto(matriz_print)
                        else:
                            print("Movimiento no valido, existe una pared.")
                    else:
                        print("Movimiento no valido, fuera de rango.")
                elif mov == "s":
                    x1 = casilla_actualx + 2
                    y1 = casilla_actualy
                    if casilla_actualx == newtamano - 2 and casilla_actualy == newtamano - 2:
                        print(f"{usuario}, You finish!")
                        break
                    elif x1 in range(newtamano) and y1 in range(newtamano):
                        if matriz_print[x1 - 1][y1] == " " and matriz_print[x1][y1] == " ":
                            matriz_print[casilla_actualx][casilla_actualy] = " "
                            casilla_actualx = x1
                            casilla_actualy = y1
                            matriz_print[casilla_actualx][casilla_actualy] = "P"
                            contador += 1
                            animacion()
                            Imprimir_laberinto(matriz_print)
                        else:
                            print("Movimiento no valido, existe una pared.")
                    else:
                        print("Movimiento no valido, fuera de rango.")
                elif mov == "salir":
                    print(f"{usuario}, You lose :(")
                    break


