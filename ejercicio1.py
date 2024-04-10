#tipo de dato y variables: integer, float, string, boolean
edad = 0
estatura = 0.0
peso = 0
nombre = ""
#print("Hola, como te llamas: ")
nombre = input("Hola, como te llamas? ")
edad = int(input("Que edad tienes? "))
estatura = float(input("Y tu estatura? "))
peso = float(input("Y tu peso? "))
imc = peso / (estatura * estatura)
print("Vaya, tu imc es: ",imc,".Ufs vamos a comer")

# <,>,>=.<=,==,!=..... python: True, False
if(edad >= 18):
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")
if(edad >= 18 and edad<=70):
 print("Eres mayor de edad")
elif(edad<18 and edad>=11):
 print("Eres menor de edad")
else:
 print("Datos no validos")