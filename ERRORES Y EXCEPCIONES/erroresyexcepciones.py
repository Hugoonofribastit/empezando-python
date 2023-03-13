def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    try:

        return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir por cero")
        return "Operación no valida"

op1 = float(input("introduce el primer valor: "))
op2 = float(input("introduce el segundo valor: "))

operacion = input("introduce la operacion a realizar(suma,resta,multiplicacion,division):")

if operacion == "suma" :
    print(suma(op1,op2))

elif operacion == "resta" :
    print(resta(op1,op2))

elif operacion == "multiplicacion" :
    print(multiplicar(op1,op2))

elif operacion == "division" :
    print(dividir(op1,op2))

else:
    print("Error: ALGO ESTA MAL")

print("Ejecutando")