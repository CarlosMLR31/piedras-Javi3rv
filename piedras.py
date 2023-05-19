import random 
import os
piedras = random.randint(12, 20)
turno = 1
def pedirPiedras():
    while True:
        try:
            piedras = int(input("Numero de piedras a quitar (1, 2 o 3): "))
            if piedras > 0 and piedras < 4:
                return piedras
            else:
                print("No has introducido un numero valido, 1, 2, o 3")
        except ValueError:
            print("No introdujiste un numero valido")

while True:
    os.system("cls")
    print(" -----------------------")
    if turno == 1:
        print("| Turno del jugador", turno, " |")
    else:
        print("| Turno del jugador", turno, " |")
    print(" ------------------------")
    print("| Piedras restantes:", piedras, " |")
    print(" ------------------------")
    piedras -= pedirPiedras()
    if piedras <= 0:
        print("ha perdido el jugador", turno)
        break
    if turno == 1:
        turno = 2
    else:
        turno = 1