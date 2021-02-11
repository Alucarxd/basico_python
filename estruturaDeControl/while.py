


#
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# repetidor de un ciclo con valor True y detenerlo

con = 0

while True:
    con += 2
    if con == 1000:
        break  # aqui se detiene por la funcion brack
    elif con == 798 or con == 898 or con == 990:
        print('Este numero no se muestra')
        continue  # aqui con la funcion continue el proceso sigue con su interecion.
    else:
        print(con)  # si no llega aqui se muestra el valor de con
print('La instruccion a terminado')
