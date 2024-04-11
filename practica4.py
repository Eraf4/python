#practica funcion
def ordenar(l,orden):
    #orden ascendente
    lista=l[:] #lista referencia
    limite = len(lista) - 1 #para no desbordar la lista
    if(orden == "ASC"):
        for x in range(0,limite):
            for y in range(0,limite):
                if lista[y] < lista[y+1]:
                    aux = lista[y]
                    lista[y] = lista[y+1]
                    lista[y+1] =aux
    #orden descendente
    elif(orden == "DESC"):
        for x in range(0,limite):
            for y in range(0,limite):
                if lista[y] > lista[y+1]:
                    aux = lista[y]
                    lista[y] = lista[y+1]
                    lista[y+1] =aux
    return lista

temperatura = [30,125,-3,100,25,-12,1,0]
lista_ordenada = ordenar(temperatura, "ASC")
print(temperatura)
print(lista_ordenada)
lista_ordenada = ordenar(temperatura, "DESC")
print(lista_ordenada)
