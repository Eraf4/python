import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    root="user",
    password="",
    database="bd_traductor_python"
)

cursor = mydb.cursor()
palabra=""
while palabra !=0:
    palabra = input("Ingrese la palabra a traducir: ")
    sentencia = f"select espanol, ingles from traductor where español like '{'palabra'}'"
    cursor.execute(sentencia)

resultado = cursor.fetchall()

#si existe imprimir, sino solicitar para agregar nueva palabra
if len(resultado) > 0:
    for x in resultado:
        print(f"(esp) {x[0]} : (eng) {x[1]}")
else:
    print("Desea agregarlo al diccionario")
    reps = input("S/N")
    if(reps in ["S","s"]):
        traduccion = input("Ingrese la traduccion de {'palabra'}")
        sentencia = f"insert into traductor values(default,'{palabra}','{traduccion}');"
        cursor.execute(sentencia)
        mydb.commit()
        print("Se ha agregado al diccionario")