personas = ["Mariano", "Pedro","Juan","Martin","Santiago","Daniel"]

print(personas)


mi_lista = ["Hugo",2,[1,2,3],["Mark"]]
print(mi_lista[3])
print(mi_lista[3][0])
print([-1]) #va a la inversa y me devuelve el array de mark, si pongo -2 me devuelve el array de numeros

#puedo poner .pop()  .popitem()solo para el ultimo elemento  .clear saca todo remove()saca el primer elemento

lista = [1,2,3,4,5]
lista.append(6)
lista

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

custom_list = ["Hola", "mundo", "mundo"] #Cuenta el número de veces que aparece un ítem

print(custom_list.count("Hola"))

["Hola", "mundo", "mundo"].index("mundo") #Devuelve el índice en el que aparece un ítem (error si no aparece

# .reverse() le da vuelta a la lista actual

#.sort() igual que en js ordena de menor a mayor
