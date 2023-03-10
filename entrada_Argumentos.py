import sys

print(sys.argv)

# entrar a la ruta de la carpeta del archivo en este caso C:\Users\Hugo\Desktop\python y poner python y el nombre de este archivo entrada_Argumentos

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error: introdujo 1 o mas de dos argumentos")
    print("Introduzca los argumentos correctamente")
    print("Ejemplo entrada_Argumentos.py 'texto' 10")
