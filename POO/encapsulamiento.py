class Auto():
    def __init__(self):
        self.__marca = "Audi"
        self.__color = "Gris Topo"
        self.__ruedas = 4
        self.__enmarcha = False
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
           return "El auto está encendido"
        else:
            return "El auto está apagado"
        
    def __str__(self):
        return f"Este auto es marca {self.__marca},de color {self.__color} y tiene {self.__ruedas} ruedas"

miCoche = Auto()

#print(miCoche.arrancar(True))

print(str(miCoche))

print("\n*****************OTRO AUTO********************\n")
miCoche2 = Auto()
miCoche2.ruedas = 6
print(miCoche2.arrancar(True))
print(str(miCoche2))
