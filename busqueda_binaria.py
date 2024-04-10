#ejercicio de busqueda binaria
import random

def busqueda_binaria(lista, comienzo, final, valor_buscado):
    print(f'----buscando {valor_buscado} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) / 2

    if lista[medio] == valor_buscado:
        print(f'Encontro {valor_buscado} Lista: {lista[medio]} Medio: {medio}')
    elif lista[medio] < valor_buscado:
        print(f'Buscando menor {valor_buscado} Lista: {lista[medio]} Medio: {medio} medio+1 {medio + 1}')
        return busqueda_binaria(lista, medio + 1, final, valor_buscado)
    else:
        print(f'Buscando mayor {valor_buscado} Lista: {lista[medio]} Medio: {medio} medio-1 {medio - 1}')
        return busqueda_binaria(lista, comienzo, medio - 1, valor_buscado)
    
if __name__ == '__main__':
    tamano_lista = int(input('Ingresa el tamaño de la lista? ')) #cambie el codigo para que el tamaño leido sea por teclado
    valor_buscado = int(input('Ingresa el valor de la lista? '))
    lista = []

    #para buscar un valor en la lista binaria esta debe estar ordenada
    lista = sorted(lista)

    existe = busqueda_binaria(lista, 0, len(lista), valor_buscado)
    print(lista)
    print(f'El elemento {existe} {"existe" if existe else "no esta"} en la lista')