a= "Hugo"
b = 30
c = "Argentina"

print("Me llamo",a, "y tengo",b,"años")

print("Me llamo {} y tengo {} años".format(a,b))
print("Me llamo {1} y tengo {0} años".format(a,b))#paso por indice y le cambio de lugar la variable
print(f"Me llamo {a} y tengo {b} años")
print("Me llamo {nombre} y tengo {edad} años y vivo en {pais}".format(nombre=a,edad=b,pais=c))
