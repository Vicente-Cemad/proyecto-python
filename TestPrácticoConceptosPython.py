# Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números
i = [2, 4]
print (min (i))

i = [-1, -4]
print (min (i))

def minimum(a, b):

    if a <= b:
        return a

    else:
        return b

a = 2

b = 4
print(minimum(a, b))

def minimum(a, b):

    if a <= b:
        return a

    else:
        return b

a = -1

b = -4
print(minimum(a, b))

#Invertir palabras de una cadena dada.
cadena = 'código de práctica de prueba de greeks'
print (cadena)
# Dividir la cadena en palabras, creando una lista
palabras = cadena.split()
print (palabras)

# Invertir las palabras, moviendose por el índice en sentido contrario
palabras_invertidas = palabras[::-1]
print (palabras_invertidas)
# Unir las palabras invertidas en una nueva cadena
cadena_invertida = ' '.join(palabras_invertidas)
print(cadena_invertida)

''' ¿?¿?¿?¿?
def rev_sentence(sentence):

    words = sentence.split(' ')

    reverse_sentence = ''.join(reversed(words))

    return reverse_sentence

if __name__ == "__main __ ":

    input = 'geeks quiz practice code'
    print (rev_sentence(input))
'''

#Realizar una suma de los elementos de una tupla
valor_tupla = (1, 1, 1, 1, 1, 1)
print (valor_tupla)

indice = 0
a = 0
print (a)

for i in valor_tupla:

    a = a + valor_tupla[indice]
    print (a)
    indice += 1

print (a)

test_tup = (1, 1, 1, 1, 1, 1)

print("The original tuple is : " + str(test_tup))

res = sum(list(test_tup))

print("The summation of tuple elements are : " + str(res))

#Escriba un código que calcule una lista de números proporcionados.

valor_lista = [1, 1, 1, 1, 1, 1, 1]
print (valor_lista)

indice = 0
a = 0
print (a)

for i in valor_lista:

    a = a + valor_lista[indice]
    print (a)
    indice += 1

print (a)

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
print(list_sum([1, 1, 1, 1, 1, 1, 1]))

#Escriba un código que desordene al azar una lista.

from random import shuffle
x = ['Skyrim', 'Pertenece', 'A', 'Los', 'Nordicos' ]
shuffle(x)
print(x)

#Escriba un codigo que pueda contar todas las palabras mayusculas de un archivo.
'''
with open(archivo) as fh:
count = 0
text = fh.read()
for character in text:
    if character.isupper():
        count += 1
'''

def contar_palabras_mayusculas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            contador_mayusculas = sum(1 for palabra in palabras if palabra.isupper())
        return contador_mayusculas
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return 0

# Ejemplo de uso
nombre_archivo = 'mi_archivo.txt'
total_mayusculas = contar_palabras_mayusculas(nombre_archivo)
print(f"Total de palabras en mayúsculas: {total_mayusculas}")

#¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print (lista1[-1])
a = lista1
print (a)
a = lista1[::-1]
print (a)

#Escriba un programa para producir la serie Fibonacci en Python.

n=10 #int(input("Introduzca el número de valores de 'n': ") )
first=0
second=1

sum=0

count=1
print("Secuencia de Fibonacci: ")
while(count <= n):
    print(sum)
    count+=1
    first=second
    second=sum
    sum=first+second

#Escriba un programa en Python para comprobar si un numero es primo.

def isPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                print (i)
                return False
        print (i)
        return True

def app():
    num = 2 #int (input('Escriba un numero: '))
    result = isPrimo (num)

    if result is True:
        print ('El número es primo! !')
    else:
        print ('El número no es primo !! ')

app()

'''
if __name__ == '__main__':
    app()
'''

'''
Escribir un programa en Python para comprobar si un número es capicúa. 
Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.
'''

numero1 = [1, 2, 1] #input(a)
print (numero1)
numero2 = numero1[::-1]
print (numero2)

if numero1 == numero2:
    print ('capicua')
else:
    print ('no capicua')

#Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
lista1 = [1, 5, 3, 4, 2]
print (lista1)
lista1.sort()
print (lista1)

lista1 = ["1", "5", "3", "4", "2"]
print (lista1)
lista1.sort()
print (lista1)

lista = ["1", "4", "0", "6", "9"]
print (lista)
lista = [int(i) for i in lista] # ¿es necesario? desaparecen las "" al convertilo de string a int
lista.sort ()
print (lista)

'''
12. ¿Cuál de las siguientes declaraciones es inválida?

a) abc = 1.000.000

b) a b b c = 1000 2000 3000

c) a,b,c = 1,000,000

d) a_b_c = 1,000,000

Solución: b) a b b c = 1000 2000 3000

Porque en los nombres de variables, no se permiten espacios.'''

#¿Cual es el resultado de ejecutar el siguiente código?

'''
try:

    if '1' != 1:
        raise "algún error"
    else:
        print("no se ha producido algún error")
except "algún error":
    print ("se ha producido algun error")

a) Se ha producido algún error

b) No se ha producido algun error

c) Código inválido

d) Ninguno de los anteriores

Solución: c) código inválido'''

try:

    if '1' != 1:
        print ('algún error')
        raise
    else:
        print("no se ha producido algún error")
except:
    print ("se ha producido algun error")

class mi_excepcion(Exception):
    pass
try:

    if '1' != 1:
        print ('algún error')
        raise mi_excepcion("se ha producido algun error")
    else:
        print("no se ha producido algún error")
except mi_excepcion as e:
    print (e)

#¿Como se puede acceder al último índice de una lista?
'''
Respuesta: Supongamos que la lista1 es [2, 33, 222, 14, 25], 
Entonces mediante, lista1 [-1] obtendremos el ultimo índice de la lista. Es decir, 25.
'''

lista1 = [2, 33, 222, 14, 25]
print (lista1)
print (lista1[-1])

tupla1 = (2, 33, 222, 14, 25)
print (tupla1)
print (tupla1[-1])
