
texto = input("Introduce un texto: ")
nombre_fichero = 'archivo' + 'texto' + '.txt'
f = open(nombre_fichero, 'w') #apertura w=write, r=read, a=append

for x in range(100):
    f.write(f'{texto} {x}\n')

f.close()
