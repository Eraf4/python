#buscar palabras ofensivas dentro de una web
from urllib import request
from urllib.error import URLError
lista_palabras = ['homosexual','prostituta','obeso','cajetuda','hijo de puta ','cabrón ','carajo','mamón','coño','culiao','pendejo','Huevón']

def verificar_palabras(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La palabra no existe!')
    else:
        aux = f.read()
        contenido = aux.split()
        palabras_encotradas = []
        for l in lista_palabras:
            for con in contenido:
                if l in con.decode():
                    palabras_encotradas.append(l)
        return palabras_encotradas
    
url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("Informe de sitio:")
print("\n---------------------------------\n")
print(verificar_palabras(url))