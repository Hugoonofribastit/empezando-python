def miPrimeraFuncion():
    print("hola desde la funcion")

miPrimeraFuncion()

i=20 #variable global

def sumar():
    i = 10 #variable local de la funcion
    print(i)
sumar()
print(i)