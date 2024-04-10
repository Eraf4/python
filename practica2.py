usuarios_autenticados = {"admin":"12345","moios":"1988","camila":"2025"}

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if(usuario in usuarios_autenticados):
    if(usuarios_autenticados[usuario] == password):
        print("ACCESO CORRECTO")
    else:
        print("ERROR DE CONTRASEÑA")
else:
    print("El usuario no existe")