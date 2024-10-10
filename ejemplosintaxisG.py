G = 'Esta variable es de ámbito Global (de módulo 1)'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep = '\n')
    f2()
f1()

G = 'Esta variable es de ámbito Global (de módulo 2)'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
    f2()
f1()

G = 'Esta variable es de ámbito Global (de módulo 3)'
def f1():
    E ='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
    def f3():
        # print(L) # DEVUELVE ERROR
        print('DEVUELVE ERROR')
    f2()
    f3()
f1()

G = 'Esta variable es de ámbito Global (de módulo 4)'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
    def f3():
        print(E, G, sep = '\n') 
    f2()
    f3()
f1()

def suma(a, b):
    return a+b

print (suma(2, 3))

print (suma(40, 30))

def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b

a, b = 5, 10

print(suma(a, b))

print(a, b) # a y b no han cambiado fuera de la función

def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print(l)
print(minimo(l)) # Modifica la lista aquí
print(l)

def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print(minimo(l[:])) # minimo modifica la lista aquí
print(l)

def f(a, b, c):
    print(a, b, c)
f(1, 2, 3)

def f(a, b, c):
    print(a, b, c)
f(c=12, a=10, b=100)

def f(a, b=10, c=30):
    print(a, b, c)
f(1)
f(1, 12)
f(1, 12, 19)

def f(a=0, b=10, c=30):
    print(a, b, c)
f()
f(1)
f(1, 12)
f(1, 12, 19)

def f(*args): # Acepta número arbitrario de argumentos
    print(args)

f() # Si no hay argumentos, args es una tupla vacía
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6)

def f(**Kargs): # Acepta número de argumentos por nombre
    print(Kargs)

f() # Si no hay argumentos, Kargs es un diccionario vacío
f(a=1)
f(a=1, b=2)
f(a=1, c=3, b=2)

def f(**kargs): # Acepta número de argumentos ¿¿¿¿¿????

    {}
{'a': 1}
{'a': 1, 'b': 2}
{'a': 1, 'c': 3, 'b': 2}

print ('ver')



def f(a, b, c, d):
    print(a, b, c, d)

argumentos = {'b':20, 'a':1, 'c':300, 'd':4000}

f(**argumentos) # Desempaquetando diccionario argumentos con **

argumentos = {'b':200, 'c':300, 'd':400}
f(10, **argumentos) # Podemos combinar argumentos posicionales con dict

def f(a, *, b, c): # Define 'b' y 'c' como keyword-only con el *
    print(a, b, c)

f(1, b=10, c=100) # Sentencia correcta
# f(1, 10, 100) Error al no pasar argumentos Keyword-only

def f(a, *b, c): # Hay que pasar 'c' por clave obligatoriamente
    print(a, b, c)
f(1, c=2)
f(1, 2, c=3) 
f(1, 2, 3, 4, 5, c=10)

la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list('ABCDE')

zlist = list(zip(la, lb, lc))
# zip soporta cualquier número
# de argumentos posicionales

zlist
a, b, c = zip(*zlist) # El * en zip desempaqueta lista de tuplas

print(la, lb, lc, sep = '\n') 
print(la, lb, lc) # Seperador por defecto es espacio
