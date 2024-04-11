notas =[]
#leer datos
for x in range(3):
    nota = int(input(f"Ingrese la nota {x}: "))
    notas.append(nota)
#calcular el promedio y si esta aprobado o reprobado
    promedio = (nota+nota)/x
#mejorar para cada nota
if(promedio>1.7):
    print("Aprobado",notas)
else:
    print("Reprobado",notas)