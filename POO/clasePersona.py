class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad= edad
        self.genero = genero

    def datosPersonales(self):
        print("______________________________")
        print("La persona se llama: ", self.nombre)
        print(f"Tiene: {self.edad} años")
        print(f"Es de genero {self.genero}")        

persona1 = Persona("Hugo", 30, "Masculino")
persona2 = Persona("Goku",50,"Masculino")

persona1.datosPersonales()
persona2.datosPersonales()
