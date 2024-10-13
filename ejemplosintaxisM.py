# Entrada input del usuario
nombre = input('Introduce tu nombre: ')
# Salida
print("Hola, " + nombre)
print(type(nombre))

# Entrada por parte del usuario como número entero
num = int(input('Introduce un número: '))
add = num+1
# Salida
print(add)
print(type(num))
print(type(add))

a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end = " ")
print(a, b, c)
'''
List = list()
Set = set()
l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del Set: "))
print("Introduzca los elementos de la lista:")
for i in range(0, 1):
    List.append(int(input()))
print("Introduzca los elementos del Set: ")
for i in range(0, 5):
    Set.add(int(input()))
print(list)
print(set)
'''
mi_lista = list()
mi_set = set()

l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del set: "))

print("Introduzca los elementos de la lista:")
for i in range(l):
    mi_lista.append(int(input()))

print("Introduzca los elementos del set:")
for i in range(s):
    mi_set.add(int(input()))

print(mi_lista)
print(mi_set)

T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzca el nuevo elemento: ")))
T = tuple(L)
print("Tupla final")
print(T)

print("GFG")
print('G', 'F', 'G')

print("GFG", end = "@")
print('G', 'F', 'G', sep = "#")

# Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida
print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))

# Declaramos una variable

nombre = "Antonio"
# Salida
print(f'hola {nombre}!. Qué tal?')
print('hola {}!'.format(nombre))

'''
%d – entero
%f – flotante
%s - cadena
%x - hexadecimal
%o – octal
'''

# Entrada de datos
numero = int(input("Introduzca un número: "))
ade = numero+5
# Salida
print("La suma es %d" %ade)
