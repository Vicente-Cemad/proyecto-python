def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    
    return a+b # "return" devuelve el resultado de la función.

print (suma(2, 3))

# Llamada a la función. Hay que pasarle dos parámetros.
# Resultado: 5

def en_pantalla(frase1, frase2):

    print (frase1, frase2) # "return" no es obligatorio

en_pantalla('Me gusta', 'Python')

# Resultado: Me gusta Python

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    a+b # Si no se pone "return" devuelve "none".

x = suma (2, 3) # Guardamos el resultado en x 

print(x) 

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

x = suma (2, 3) # Guardamos el resultado en x 

print(x) 

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.

    return a+b # "return" devuelve el resultado de la función.

print (suma (2, 3)) 
x = suma (2, 3)
print (x)

# Función con ints
# Resultado = 5

print (suma(2.7, 4.0)) 
x = suma (2.7, 4.0)
print (x)

# Función con floats
# Resultado = 6.7

print (suma('Me gusta', 'Python')) # Función con strings
x = suma ('Me gusta', 'Python')
print (x)

def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)

    b = 100

    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1

    f2(b)

f1('Python') # Llamamos a f1

'''
calcula el factorial de 
un número (recordemos que el factorial de x es igual 
a x * (x-1) * (x-2) * … * 1
'''

def factorial(x):

   if x>1:
        return x*factorial(x-1)
   else:
        return 1
   
print (factorial(5))

def maxmin(lista):

    return max(lista), min(lista) # Devuelve una tupla de 2 elementos

l = [1, 3, 5, 6, 0]

maximo, minimo = maxmin(l) # Desempaqueta la tupla en 2 variables

print(minimo, maximo, sep='-')
