class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def registrar(self):
        print(f'El usuario {self.nombre} a sido registrado')
    # def __str__(self):
    #     print(f'El usuario se llama {self.nombre} y su edad es de {self.edad}')
    def consultar_tipo(self):
        print('Sin especificar')


class Empleado():
    def __init__(self, area_trabajo):
        self.area_trabajo = area_trabajo
    def generar_reporte(self):
        print(f'Generando el reporte del empleado del area de {self.area_trabajo}')

# heredando los metoodos y  atributos de la clase Usuario
class Cliente(Usuario):
    def __init__(self, nombre, edad, n_compras):

        super().__init__(nombre, edad)
        self.n_compras = n_compras

    def ver_compras(self):
        print(f'El numero de compras del cliente {self.nombre} es {self.n_compras}')
    def consultar_tipo(self):
        print('El tipo de usuario es cliente')


# herencia multiple
class Vendedor(Usuario, Empleado):

    def __init__(self, nombre, edad, area_trabajo ,n_ventas):
        Usuario.__init__(self, nombre, edad)
        Empleado.__init__(self, area_trabajo)
        self.n_ventas = n_ventas

    def ver_ventas(self):
        print(f'El numero de ventas del vendedor {self.nombre} es {self.n_ventas}')
    def consultar_tipo(self):
        print('El tipo de usuario es vendedor ')


usuario = Usuario('Nombre...', 22)
cliente = Cliente('Nombre..', 23, 421)
vendedor = Vendedor('Nombre...', 21, 'ventas', 200)

# esta adoctando muchas formas, se lo conoze como poliformismo
# def mostrar_tipo(objeto):
#     objeto.consultar_tipo()
# mostrar_tipo(cliente)
#  Aqui mostrare todos
for object in (usuario, cliente, vendedor):
    object.consultar_tipo()
