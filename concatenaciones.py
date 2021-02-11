print('Hola ' + 'Mundo')

print('Mi nombre es {} {}'.format('Gabriel', 'Garcia'))

print('Mi nombre es {0} {1} bienvenido al curso de {2}'.format('Gabriel', 'Garcia', 'Python'))  

print('Mi nombre es {1} {0} bienvenido al curso de {2}'.format('Gabriel', 'Garcia', 'Python')) # Aqui estoy dando preferencia a la secuencia (en este caso esta variando)

print("Mi nombre es {} {} bienvenido al curso de {}".format(input('Ingrese su nombre: '), input('Ingrese su apellido: '), input("Nombre del curso?: "))) # inplementando input a la funcion .format

# print('Mi nombre es {0} {1} bienvenido al curso de {2}'.format(input('Ingrese su nombre: '),input('Ingrese su apellido: '), 'Python'))