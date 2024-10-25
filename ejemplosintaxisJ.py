a = 10
b = 3
if a > b:
    print ('SI se cumple la condición') 
# Bloque identado 4 espacios

print ('Ya estamos fuera del if') 
'''SI se cumple la condición
Ya estamos fuera del if
'''

a = 10
b = 3
if a > b:
    print ('Se ha cumplido la condición') 
else:
    print ('No se ha cumplido la condición')

print ('Ya estamos fuera del if')
'''No se ha cumplido la condición
Ya estamos fuera del if
'''

a = 3
b = 10
if a > b:
    print ('Se ha cumplido la condición') 
else:
    print ('No se ha cumplido la condición')

print ('Ya estamos fuera del if')
'''No se ha cumplido la condición
Ya estamos fuera del if
'''

a = 10
b = 10
if a > b:
    print ('A es menor que B') 
elif a == b:
    print ('A es igual a B')
else:
    print ('A es mayor que B')

print ('Ya hemos salido del condicional')
'''A es igual a B
Ya hemos salido del condicional
'''

a=10
b=3

if a>b:
    print('true_value')
else:
    print('false_value')

print('true_value') if a > b else print('false_value')

x = (print('true_value') if a > b else print('false_value'))

#COMO SABER SI UN VALOR ES NUMERICO
#EJEMPLO CON LISTA
l = list()
print(l)
texto = input("Introduce un numero entero por teclado: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print("Número " + str(num) + " añadido a la lista")
    print(l)
else:
    print("No has introducido un número entero")
    print(l)

#EJEMPLO CON DICCIONARIO

d = { "50862634" : 37 , "43394932" : 32}
print(d)

texto = input("Introduce un documento de indentidad ")

if texto in d:
    print("La edad de " + texto + " es " + str(d[texto]))
    print(d)
else:
    edad = input("Documento no existente. Introduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("Añadido al diccionario")
        print(d)

#Mostramos por pantalla el diccionario
print(d)

'''Veamos un ejemplo sencillo para leer un archivo y
guardarlo en un diccionario:
'''

# read python dict from a file
#pkl_file = open('myfile.pkl', 'rb')
#mydict2 = pickle.load(pkl_file)
#pkl_file.close()

'''Y ahora veamos cómo escribir un diccionario en un
archivo:
'''

# write python dict to a file
#mydict = {'a': 1, 'b': 2, 'c': 3}
#output = open('myfile.pkl', 'wb')
#pickle.dump(mydict, output)
#output.close()

#COMO TRABAJAR CON DICCIONARIOS Y FICHEROS, SALVAR Y RECUPERAR DICCIONARIOS DE FICHEROS

import pickle
from pathlib import Path

print (Path)

#Create an empty dictionary
d= dict()

#Ask for file name to load dictionary from
file_name = input("Introduce el nombre del archivo con los datos: ")

#Comprobamos que existe
path = Path(file_name)
if path.is_file():
    # Open file in reading mode
    input_file = open(file_name, 'rb')
    d = pickle.load(input_file)
    #Close de file
    input_file.close()
else:
    print("El file no existe, creamos diccionario vacio")

#Check for values or add new ones
document_number = input("Introduce un documento de indentidad ")

if document_number in d: #Check whether it is on dict or not
    print("La edad de " + document_number + " es " + str(d[document_number]))
else:
    age = input("Documento no existente. Introduce edad: ")
    if age.isnumeric():

        num = int(age)
        d[document_number] = num
        print("Añadido al diccionario")

# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()

a = 0
while a<3:
    print (a, end=' ') # Acabamos con espacios en lugar de salto de línea
    a += 1 # Equivalente a: a = a + 1

print (a) # Estamos fuera del while
print('Hemos salido fuera del while')

# 0 1 2 3 
# Hemos salido fuera del while

# BREAK
a = 5
while a: # Utilizamos la propia variable como condición
    print (a, end=' ')
    if a == 2 :
        break
    a -= 1

print ('\nFuera del Bucle.')
print('Valor de "a": {}'.format(a))

#5 4 3 
#Fuera del Bucle.

# CONTINUE
a = 7
while bool(a):
    a -= 1
    if a % 2 == 0 :
        continue # Saltamos a la siguiente iteracción si es a es par.
    print (a, end=' ')

print ('\nFuera del Bucle.')

#5 3 1
#Fuera del Bucle.

# PASS
a = 5
while a:
    pass # Presiona Ctrl-C para abortar la ejecución
    print (a)
    break #Rompe el while

# ELSE
a = 13
b = a // 2 # División entera. P. ej. 13 // 2 == 6

while b > 1:
    if a % b == 0: # % es el operador resto. P. ej. 10 % 5 == 0
        print('{b} es factor de {a}'.format(b,a)) # OJO DA ERROR EN LA EJECUCIÓN
        break
    b -= 1
else:
    print('{} es primo'.format(a))

print ('\nFuera del Bucle.')

#13 es primo
#Fuera del Bucle.
