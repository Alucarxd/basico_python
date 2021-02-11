class Usuario:

    def __init__(self):
        # con esto especifico que es un metodo privado __
        self.__nombre = 'Ana'
        self.__edad = 23

    # Getter permiten consultar a los met o atri, privados
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return  self.__edad

    # Setter permite dar valor a los met o atri, privados
    def setNombre(nombre):
        if nombre == 'Ana':
            self.__nombre = nombre
        else:
            return 'No puedes asiganr ese nombre'

    def setEdad(edad):
        if edad == 23:
            self.__edad = edad
        else:
            return 'No puedes asiganr ese edad'



    def __registar(self):
        print(f"El usuario {self.__nombre} ha sido registardo")
    def __str__(self):
        print(f"El usuario se llama {self.__nombre} y su edad es {self.__edad}")
    def consultar_tipo(self):
        print("Sin especificar")

usuario = Usuario("Pablo", 3)
# print(usuario.nombre)
# print(usuario.edad)
# usuario.registar()
print(usuario.getNombre())
print(usuario.getEdad())