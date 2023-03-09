""" i = 0

while i<= 10:
    print("holis", i)
    i+=1 
else:
    print("adios, me voy del bucle")

 """


""" edad = int(input("ingrese su edad: "))

while edad < 0:
 print("edad incorrecta")
 edad = int(input("ingrese su edad"))
else:
   print("gracias, su edad es:",edad, "años") """


i = 0
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        continue
    print("continuo")
    if i == 4:
        print("me voy de aqui")
        break