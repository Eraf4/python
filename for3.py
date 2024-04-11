for x in range(5):
    print("*" * x)

for x in range(5):
    print("*" * (x+1))

for x in range(5):
     if x==0 or x==4:
         print("*" * 5)
     else:
         print("*    *")
#solo bores????
tabelro = [
    ['h','o','l','a','s'],
    ['o','s','m','a','l'],
    ['l','u','c','h','i'],
    ['a','i','r','a','m'],
    ['s','l','i','m','e']
]
fila= 5
columna=5
aciertos=0
errores=0
for f in range(fila):
    for c in range(columna):

        if(f==0 or f==(fila - 1) or c==0 or c == (columna-1)):
            print(tabelro[f][c],end=' ')
        else:
            print(" ",end=' ')
            
print(end='\n')