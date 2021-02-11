class Persona:
    # Clase inicializadora
    def __init__(self, nombre, edad):
        # Atributos
        self.nombre = nombre
        self.edad = edad

    # Metodo
    def caminar(self):
        print(f'{self.nombre} esta caminando')
    def correr(self):
        print(f'{self.nombre} esta corriendo')

    def __str__(self):
        return f'La persona se llama {self.nombre} y su edad es {self.edad}'
# creando los objetos ( instancias )
persona = Persona('Gabriel', 21)
persona2 = Persona('Gabriel', 21)
persona3 = Persona('Gabriel', 21)
print(persona)
persona2.correr()
persona3.caminar()





