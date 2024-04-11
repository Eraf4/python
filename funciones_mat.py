#funciones matematicas

def suma(a,b):
    return a + b

def resta(a,b):
    return a +- b    

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if(b == 0):
        return "no se puede dividir por CERO"
    else:
        return a/b
def raiz(a,b = 2):
    return a * (b*1/2)
#cuando ejecutamos es script, __name__ para ser igual al string '__main__'
if __name__ == "__main__":
    resultado1 = suma(3,4)
    resultado2 = resta(3,4)
    resultado3 = multiplicacion(3,4)
    resultado4 = division(3,4)
    resultado5 = raiz(3,4)
    print(resultado1)
    print(resultado2)
    print(resultado3)
    print(resultado4)
    print(resultado5)
    
#implementa y ejcuta las otras funciones