for s in ['Me', 'gusta', 'Python!']:
    print(s, end=' ')
#Me gusta Python!

a = 0
for x in [1, 2, 3, 4]:
    a += x

print(a)

#10

for c in 'Me gusta Python!':
    print(c, end=' ')

#M e g u s t a P y t h o n !

e = {'a': 'Apellidos', 'b': 'edad', 'c': 'nombre'}


for j in e.keys():
    
    print (j)


for j in e.values():
    
    print (j)

lista = []
lista.extend(e.values())
print (lista[0])
print (lista[1])
print (lista[2])
#Apellidos edad nombre

keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k]) 
    print (info)

# Texto formateado con claves y valores
'''
Apellidos: van Rossum
edad: 60
nombre: Guido'''

a, b = (3, 4) # Asignamos los elementos de la tupla a cada variable
print(a, b)
#3 4

t = [(1, 2), (3, 4), (5, 6)]
for x, y in t:
    print (x + y, end= ' ')
#3 7 11

la = [10, 20, 30, 40]
lb = [5, 25, 50, 10]
for a, b in zip(la, lb):
    m = max(a, b) # max(a, b) devuelve el máximo entre a y b
    print(m , end=' ')
#10 25 50 40

keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values)) 
for k, v in d.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))
'''apellidos: van Rossum
edad: 60
nombre: Guido'''

for k in d.keys():
    print(k, end= ' ')
#apellidos edad nombre
for v in d.values():
    print(v, end= ' ')
#Van Rossum 60 Guido

import random
letras = list('abcdefghijklmnopqrstuvwxyz')
l1 = letras[:8]
l2 = letras[8:16]
l3 = letras[16:]

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

for i in range(len(l1)):
    print(l1[i] +l2[i]+l3[i], end=' ')

#cpv emq dlt hnr fis gow akz bjx

for a, b, c in zip(l1, l2, l3):
    print(a + b + c, end=' ')

#cpv emq dlt hnr fis gow akz bjx

# Creamos 3 sub-listas a partir de trozos

# Barajamos cada trozo

# Versión NO Pythónica. NO RECOMENDADA

# Versión Pythónica.

letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random.shuffle(letras)
print(''.join(letras))
#rqkmjgvzblsaoicfntxewduphy

for i in range(len(letras)):
    if letras[i] in vocales:
        print('{} en la posición {}'.format(letras[i], i))

'''
a en la posición 11
o en la posición 12
i en la posición 13
e en la posición 19
u en la posición 22
'''

for i, letras in enumerate(letras):
    if letras in vocales:
        print('{} en la posición {}'.format(letras, i))

'''
a en la posición 11
o en la posición 12
i en la posición 13
e en la posición 19
u en la posición 22
'''

# Manera NO Pythónica

# Manera Pythónica

# Ejemplos de enumerate. Hay que envolverlo en list() o recorrerlo en un for
abcde = sorted(letras)[:5]

list(enumerate(abcde))
#[(0, 'a'), (1,'b'),(2, 'c'),(3,'d'), (4,'e')]

list(enumerate(abcde, 10))
#[(10, 'a'), (11, 'b'), (12, 'c'),(13, 'd'), (14, 'e')]

# Devuelve secuencia con sus índices

# Podemos decirle en qué índice empieza

for num in [1, 2, 3, 4, 5, 6]:
    print(num ** 2, end= ' ')
#1 4 9 16 25 36
for num in [12, 38, 99, 1]:
    print(num / 2, end= ' ')
#6.0 19.0 49.5 0.5
for letra in 'Python':
    print(letra.upper(), end=' ')
#P Y T H O N

zen = '''\
... Bello es mejor que feo.
... Explícito es mejor que implícito.
... Simple es mejor que complejo.
... Complejo es mejor que complicado.
... '''

f = open('.\short.zen.txt', 'w')
f.writelines(zen) # Escribe el fichero
f.close() # Cierra el fichero

f = open('.\short.zen.txt', 'r')
print(f.readline())
#'Bello es mejor que feo. \n'

print(f.readline())
#'Explícito es mejor que implícito. \n'

print(f.readline())
#'Simple es mejor que complejo. \n'

print(f.readline())
#'Complejo es mejor que complicado. \n'

print(f.readline())
f.close() # Cierra el fichero
# Devuelve una cadena vacía cuando termina el fichero

#Traceback (most recent call last)

f = open('.\short.zen.txt', 'r')

print (f.__next__())

#'Bello es mejor que feo. \n'

print (f.__next__())
#'Explícito es mejor que implícito. \n'

print (f.__next__())
#'Simple es mejor que complejo. \n'

print (f.__next__())
'Complejo es mejor que complicado. \n'

print (f.__next__())

StopIteration
f.close() # Cierra el fichero

'''
<ipython-input-55-39ec527346a9> in <module>()
>1 f ._ next_()'''

#StopIteration:

for linea in open('.\short.zen.txt', 'r'):
    print(linea.upper(), end='')
f.close() # Cierra el fichero

'''
BELLO ES MEJOR QUE FEO.
EXPLÍCITO ES MEJOR QUE IMPLÍCITO.
SIMPLE ES MEJOR QUE COMPLEJO.
COMPLEJO ES MEJOR QUE COMPLICADO.'''

f = open('.\short.zen.txt', 'r')
print (f.__next__())
#'Bello es mejor que feo.\n'
print (next(f))
#'Explícito es mejor que implícito.\n'
print (next(f))
#'Complejo es mejor que complicado.\n'
print (next(f))
'''
-----------------------------------------
StopIteration Traceback(most recent call last)
<ipython-input-77-468f0afdf1b9> in 
<module>()
----> 1 next(f)
'''

StopIteration

f.close() # Cierra el fichero

lista = [1, 2, 3]
li = lista.__iter__()
print(li.__next__())
#1
print (next(li))
#2
print (next(li))
#3
#print (next(li))

'''
-----------------------------------------
StopIteration 
Traceback(most recent call last)
<ipython-input-91-deb767b63ff8> in 
<module>()
----> 1 next(li)
'''

StopIteration

li = iter(lista)
print (next(li))
#1
print (next(li))
#2
print (next(li))
#3
#print (next(li))

'''
-----------------------------------------
StopIteration Traceback(most recent 
call last)
<ipython-input-95-deb767b63ff8> in 
<module>()
----> 1 next(li)
'''
StopIteration

'''
rep = Repetidor(3, ):

def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0

def __next__(self):
    if self.counter == self.veces:
        raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item
'''
'''         
class Repetidor(3, 'Python', ):
    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0

    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item
'''        

#Objeto iterador no iterable, incorpora el metodo next pero no el metodo iter
class Repetidor:
    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0

    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item

#Lectura de un iterador no iterable ya que contiene next pero no iter
rep = Repetidor(3, 'a')
print (next(rep))
print (next(rep))
print (next(rep))

#Objeto iterador al incorporar next e iterable al incorporar iter
class Repetidor:
    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item

#uso de un iterador iterable al incorporar los métodos next e iter
#los bucles for llaman a la clase iter
rep = Repetidor(3, 'a')
for item in rep:
    print(item)
    StopIteration

#tambien se pueden crear iterables con iter pero no iteradores al faltarles la clase next
class Repetidor():
    def __init__(self, veces, *items):
        self.veces = veces
        self.items = items

    def __iter__(self):
        return iter(self.items * self.veces)

rep = Repetidor(3, 'a', 'b', 'c')
#next(rep) #da error al no ser un iterador
for r in rep:
    print(r, end=' ')
