#lista
milista = [1, 2, 3, 4, 5]
print (milista)
print (milista[:])
print (milista[:2])
print (milista[2:])
print (milista[:-2])
print (milista[-2:])
print (milista[1:2])
print (milista[1:2:2])

#tupla
mitupla = (1, 2, 3, 4, 5)
print (mitupla)
print (mitupla[:])
print (mitupla[:2])
print (mitupla[2:])
print (mitupla[:-2])
print (mitupla[-2:])
print (mitupla[1:2])
print (mitupla[1:2:2])

x = ("apple", "banana", "cherry")
print (x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
print (thistuple)
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print (thistuple)

thislist = list("apple")
print(type(thislist))
print (thislist)

thislist = "apple"
print(type(thislist))
print (thislist)

thistuple = tuple("apple")
print(type(thistuple))
print (thistuple)

thistuple = ("apple",)
print(type(thistuple))
print (thistuple)

thistuple = ("apple")
print(type(thistuple))
print (thistuple)

print ('inicio')
miTupla="Angel", 4, 5.345, True, 4
'''Desempaquetado de tupla. Permite asignar 
todos los elementos de una tupla a 
diferentes variables:'''
print (type(miTupla))
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)
print (type(miTupla))

milista="Angel", 4, 5.345, True, 4
'''Desempaquetado de LISTA. Permite asignar 
todos los elementos de una LISTA a 
diferentes variables:'''
print (type(milista))
milista=["Angel", 4, 5.345, True, 4]
nombre, num1, num2, valor1, num3=milista
print (type(milista))
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)
print (type(milista))

#diccionarios
dic = {
    "Nombre":"Santiago",
    "Apellido":"Hernandez",
    "Pais":"España",
    "Ciudad":"Madrid"
    }
print(dic)
print (type(dic))
# Otra forma de definir diccionarios con la funcion dict()
dic2 = dict(
    Nombre="Santiago",
    Apellido="Hernandez",
    Pais="España",
    Ciudad="Madrid"
    )
print(dic)
print (type(dic))
