#Clases y Objetos

class Gelatina:
    def __init__(self,sabor,color,tamaño):
        self.sabor = sabor
        self.color = color
        self.tamaño = tamaño
    
    def imprimir(self):
        print("____________________________\n")
        print("La gelatina es de "+self.sabor)
        print("La gelatina es de color "+self.color)
        print("La gelatina es de tamaño "+self.tamaño)
       

gel1 = Gelatina("Frutilla","roja", "Grande")
gel2 = Gelatina("Mora","Azul", "Chica")
gel3 = Gelatina("Naranja","naranja", "Mediana")
gel4 = Gelatina("Manzana","Verde", "Grande")

gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()
