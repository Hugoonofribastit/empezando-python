def retornarTexto():
    return "Texto"
#print(retornarTexto())
 


def suma(num1, num2):
    resultado = num1 + num2
    return resultado

#print(suma(4,5))



# ARGUNMENTOS INDETERMINADOS

def infinit(*args): 
    for args in args:
        print(args)

#infinit("Hola",20,10,15,[1,2,3])

#indeterminados con claves
def infinitWithKeys(**kwargs):
    #print(kwargs)
    for kwarg in kwargs:
        print(kwarg,"--->",kwargs[kwarg])

infinitWithKeys(a="Hola", b= 3, c=True,d =["Juan","Peter","Tincho"])

 