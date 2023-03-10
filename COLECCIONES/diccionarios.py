mi_diccionario = {1:"Mark",2:"Tom",3:"Luna",4:[1,2,3]}
# mi_diccionario = dict({1:"Mark",2:"Tom",3:"Luna",4:[1,2,3]}) ES LO MISMO

print(mi_diccionario[1]) #accedo desde el elemento 1 como el primer elemento

print(mi_diccionario.get(4)[0])

mi_diccionario[4] = ["Hola"]
print(mi_diccionario)

