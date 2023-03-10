def miPrimeraFuncion():
    print("hola desde la funcion")

miPrimeraFuncion()

i=20 #variable global

def variableI():
    i = 10 #variable local de la funcion
    print(i)
variableI()

print(i)#variable global


def suma():
    x = 10
    y = 20
    resultado= x + y
    print(f"El resultado de la suma es: {resultado}")
suma()