#numeros primos
numero = 100
while True:
    bandera = 0
    for x in range(2, numero-1):
        if(numero % x == 0):
            bandera = 1
            #si bandera es 1 ya no es primo
            break

    if(bandera == 0):
        print(numero)
    break
numero = numero + 1
    