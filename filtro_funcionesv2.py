print("Ingrese 5 números")
def filtrar(numero):
    if 0 < numero <= 100:
        print(f"El número {numero} está dentro del rango de 1 a 100.")
        return True
    elif numero > 100:
        print(f"El número {numero} es mayor que 100.")
        return False
    else:
        print(f"El número {numero} debe estar entre 1 y 100.")
        return False

def ingresar_numero():
    lista_numero = []
    cont = 0
    while cont < 5:
        try:
            ingreso_numero = int(input("Ingresar un número: "))
            if filtrar(ingreso_numero):
                lista_numero.append(ingreso_numero)
                cont += 1
        except ValueError:
            print("Error: debe ingresar un número entero.")
    print("Los números ingresados son:", lista_numero)

ingresar_numero()