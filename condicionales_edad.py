edad = int(input("Ingrese su edad: "))
#licencia de conducir
#menor de edad con permiso de padres: 15 y 17
#mayor de edad de 18 a 64 licencia estandar
#65 años hasta 75 debe hacer test psicotecnico

if(edad>=15 and edad<18):
    print("Licencia con permiso de padres")
elif(edad>=18 and edad <65):
    print("Licencia estandar")
elif(edad>=65 and edad<75):
    print("Primero debe realizar test sicotecnico")
else:
    print("Usted no puede obtener una licencia. Consulte con...")