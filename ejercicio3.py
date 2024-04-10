# Compuertas Logicas
A= True
B= True
Y = (not A and B) or (B and not A) or (A and B)
if( not A and B ):
    print("Verdadero")
elif(B and not A):
    print("Verdadero")
elif(A and B):   
    print("Verdadero")
else:
    print("Falso")