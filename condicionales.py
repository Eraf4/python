numero_1=int(input("Ingrese un numero: "))
numero_2=int(input("Ingrese un numero: "))

if(numero_1>numero_2):
    print("{} es mayor a {}".format(numero_1,numero_2))
    if(numero_1 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
elif(numero_1<numero_2):
    print("{} es mayor a {}".format(numero_2,numero_1))
    if(numero_2 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("Los numeros ingresados son iguales")

print("-------------------------------------")
usuario=input("Ingrese un usuario: ")
password=input("Ingrese su contraseña: ")
if(usuario=="admin" and password =="12345"):
    print("Acceso correcto")
else:
    print("Acceso denegado")
