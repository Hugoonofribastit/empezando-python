class Auto():
    def __init__(self):
        self.marca = "Audi"
        self.color = "Gris Topo"
        self.ruedas = 4
        self.enmarcha = False
    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
           return "El auto está encendido"
        else:
            return "El auto está apagado"
        
    def __str__(self):
        return f"Este auto es marca {self.marca},de color {self.color} y tiene {self.ruedas} ruedas"

miCoche = Auto()

print(miCoche.arrancar(True))

print(str(miCoche))