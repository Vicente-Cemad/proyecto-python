for i in ["primavera", "verano", "otoño", "invierno"]: 
    print(i)
# validar un mail en función de si tiene @ simplemente recorriendo la logitud del string:
valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
    if valido:
        print("Email correcto")
    else:
        print("Email incorrecto")

'''
# validar un mail en función de si tiene @ simplemente recorriendo la logitud del string:
valido=False
email=input("Introduce tu email: ")
for i in (len(email)): da error ya que es un int y no es iterable
    if email[i]=="@":
        valido=True
    if valido:
        print("Email correcto")
    else:
        print("Email incorrecto")
'''

# Imprime edad cuando el contador llegue a 18 
edad = 0
while edad < 18: 
    edad=edad+1
print("Tienes "+str(edad))

edad = 0
while edad in [0, 1, 2]: #tambien funciona la iterción con while
    print(edad)
    edad=edad+1
print("Tienes "+str(edad))

# LISTAS
"""
La lista es un tipo de colección ordenada 
y modificable. 
Es decir, una secuencia de valores de 
cualquier tipo, ordenados y de tamaño 
variable.
Se escriben entre corchetes. []
"""
miLista=["Angel", 43, 667767250] 
print (miLista)
miLista [0] = "Pedro"
print (miLista)
miLista2 = [22, True, "una lista", [1, 
2]]
# MÉTODOS DE LAS LISTAS
# Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)
# Acceder a los elementos de una lista

# TUPLAS
"""Una tupla es una colección ordenada e 
inmutable. 
En Python, las tuplas se escriben entre 
paréntesis.
"""
# Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])
# Otra forma de declararla
miTupla = tuple(("manzana", "banana", 
"cereza"))
print(miTupla)
# Indexación Negativa

# DICCIONARIOS
"""Los diccionarios, también llamados 
matrices asociativas, deben su nombre a 
que son 
colecciones que relacionan una clave y un 
valor.
Un diccionario es una colección 
desordenada, modificable e indexada. 
En Python, los diccionarios se escriben 
entre llaves y tienen claves y valores.
"""
# Declaración de un diccionario
miDiccionario = {"brand": "Ford","model": "Mustang", "year":"1964"}
print(miDiccionario)
# A los valores almacenados en un diccionario se accede por su clave
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino","Amélie": "Jean-Pierre Jeunet"}
print (peliculas["Love Actually"]) 
print(peliculas)
# Reasignar valores a un diccionario
peliculas["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

# SETs, conjuntos
"""
Un conjunto es una colección de elementos 
únicos que no está ordenada ni indexada, 
por lo que no puede estar seguro de en 
qué orden aparecerán los elementos. 
En Python, los conjuntos se escriben 
entre llaves
Una vez que se crea un conjunto, no puede 
cambiar sus elementos, pero puede agregar 
nuevos elementos.
"""
# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
# Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara", "Pilar")) 
print(mi_conjunto)
print(mi_conjunto2)
print(mi_conjunto3)
# Para añadir un nuevo elemento:
mi_conjunto.add("Antonio")
print(mi_conjunto)
# Para añadir varios elementos:
mi_conjunto.update({"Fran", "María"})
print(mi_conjunto)
# Intersección de conjuntos:
interseccion= mi_conjunto & mi_conjunto2
# Nos crea otro conjunto con los 
#valores que estaban duplicados en ambos 
#conjuntos. 
# En nuestro caso sólo Angel.
# Diferencia de conjuntos. Nos crea 
#otro conjunto con los elementos que no 
#están duplicados.
diferencia= mi_conjunto - mi_conjunto2
print (diferencia)
# Para comprobar si un elemento está en 
#un conjunto:
miSet = {"manzana", "banana", "cereza"}
for x in miSet:
    print(x)
"""
No puede acceder a los elementos de un 
conjunto haciendo referencia a un índice, 
ya que los conjuntos no están ordenados, 
los elementos no tienen índice.
"""
# Obtenga la cantidad de elementos en 
#un conjunto:

print(len(miSet))
# Elimine "banana" utilizando el método 
#remove() :
miSet = {"manzana", "banana", "cereza"}
miSet.remove("banana")
print(miSet)

# -------------------------------------
# FUNCIONES
# -------------------------------------
# Definición de una función. Importante 
#la identación:
def my_funcion():
    print("Estamos ejecutando la     función.")
# Llamada a la función. En otra parte 
#de mi código, llamamos a la función para 
#que se ejecute:
my_funcion()
# -------------------------------------
def suma():
    num1 = 3
    num2 = 5
    print("suma =", num1+num2)
suma()
# Otra opción:
def suma():
    num1 = 3
    num2 = 5
    resultado = num1 + num2
    return resultado
print(suma())
# -------------------------------------
#El bloque de código que ejecutará la 
#función incluye todas las declaraciones 
#con indentación 
# dentro de la función.
def miFunción():
    print('this will print')
    print('so will this')
miFunción()
