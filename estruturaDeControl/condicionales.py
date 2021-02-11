'''
condicional = True

if condicional:
    print("Se cumple la condicon")
else:
    print('No se cumple la condicion')

n1 = 4
n2 = 6
suma = n1 + n2

if suma == 12:
    print("Se cumple la condicon")
else:
    n1 = input("Ingrese el numero 1: ")
    n2 = input("Ingrese el numero dos: ")
    suma = int(n1) + int(n2)
    if suma == 10:
        print("Lo LOGRASTE")
    else:
        print('No se cumple la condicion')
'''
''' METODO UNO
n_ingresado = input('Ingresa un numero: ')
g = 'chao bebesito'
if n_ingresado == '1':
    print('Ingresante el numero 1!')
elif n_ingresado == '2':
    print('Ingresante el numero 2!')
elif n_ingresado == '3':
    print('Ingresante el numero 3!')
else:
    print('No ingresastes los numeros esperados ' + g)
'''
n_ingresado = input('Ingresa un numero: ')
g = 'chao bebesito'

if n_ingresado == '1' or n_ingresado == '2' or n_ingresado == '3':
    print("Ingresate los numeros correctos")
else:
    print('No ingresaste los numeros esperados ' + g)
