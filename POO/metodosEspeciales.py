class Coche:
    def __init__(self, marca,kilometros,modelo):
        self.marca = marca
        self.kilometros = kilometros
        self.modelo = modelo
        print(f"Se ha creado un auto {self.marca}, modelo {self.modelo} con {self.kilometros} kilometros")

    def __del__(self):
        print(f"Se ha vendido el {self.marca}")
    def __str__(self):
        return "El auto es un {}, tiene {}kilometros y es del año {}".format(self.marca, self.kilometros,self.modelo)
    

miCoche = Coche("Ford",9000,2020)
print(str(miCoche))
#del(miCoche)


