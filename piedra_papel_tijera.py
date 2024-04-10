import random

while True:
    aleatorio = random.randrange(0,3)
    elijePc = " "
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion = int(input("Elige tu opcion "))

    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elegiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "Piedra"
    elif aleatorio == 1:
        elijePc = "Papel"
    elif aleatorio == 2:
        elijePc = "Tijera"
    print("La Maquina eligio: ", elijePc)
    print("...")

    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste,papel envuelve a piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste,tijera corta papel")
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste,piedra machaca tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste,papel envuelve a piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("Perdiste,tijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste,piedra machaca tijera")
    elif elijeUsuario == elijePc:
        print("Empate")