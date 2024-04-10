# practica con el modulo random
#ejercicio de busqueda lineal
import random

def busqueda_lineal(lista,valor_buscado):
    existe = False

    for elemento in lista:#0(n)
        if elemento == valor_buscado:
            existe = True
            break

    return existe

if __name__ == '__main__':
    tamano_de_lista = int(input('Cual es el tamaño de la lista? ')) #Silocita por teclado el tamaño de la lista
    valor_buscado = int(input('Qué número quieres buscar en la lista? '))
    lista = []
# creamos una lista y cargamos con valores aleatorios de 0 a 100
    #lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    for i in range(tamano_de_lista):
        lista.append(random.randint(0,100))

existe_valor = busqueda_lineal(lista, valor_buscado)
print(lista)
#modifica la sentencia para que imprima en qué posicion se encuentra el valor
print(f'El número {valor_buscado}{"existe" if existe_valor else "no esta"} en la lista')