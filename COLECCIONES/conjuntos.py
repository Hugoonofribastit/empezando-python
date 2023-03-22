mi_conjunto = set({1.0,1,2,3,"Hola",(1,2,3)})
print(mi_conjunto)

#los elementos estan desordenados, no hay indexacion
#no admiten duplicados
mi_conjunto2 = {1,3}
print(mi_conjunto2)
mi_conjunto2.add(2)
print(mi_conjunto2)

mi_conjunto2.update([1,2,3,4,"Hola"])#si dentro del update le agrego una lista con los elementis 1,2,3 solamente no me los va a tomar porque el conjunto ya los tiene y asi solo me agrega los nuevos elementos
print(mi_conjunto2)

mi_conjunto2.discard(4)
print(mi_conjunto2)
mi_conjunto2.remove(2)
print(mi_conjunto2)

#podemos tambien usar el clear y sacar todo o el pop y pasarle el indice