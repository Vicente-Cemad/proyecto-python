
x = []
import numpy as np
x = list(np.random.randint(low=1, high=500000, size=99999999))
print ("Genero una lista de 100 millones de números aleatorios")

def constante(x:list) -> list:
    return x
print ("Complejidad Constante O(k) Constant Time")
constante(x)

def iterador_normal(x:list) -> list:
    contador = len(x)
    while(contador > 0):
        contador -= 1
    return x
print ("Complejidad O(n) Linear Time")
iterador_normal(x)

def iterador_anidado(x:list) -> list:
    contador_externo = len(x)//1000
    contador_interno = len(x)//1000
    while(contador_externo > 0):
        contador_externo -= 1
        for i in range(contador_interno):
            i
    return x
print ("Complejidad O(n2)Quadratic Time")
iterador_anidado(x)

def iterador_multiplicado(x:list) -> list:
    iterador = len(x) 
    incremento = 1
    while(iterador > 0):
        iterador -= incremento
        incremento *= (incremento + 1)
    return x
print ("Complejidad O(log(n)) Logarithmic Time")
iterador_multiplicado(x)

def iterador_dividido(x:list) -> list: 
    iterador = -len(x) 
    incremento = 1
    while(iterador < 0):
        iterador /= incremento
        incremento += 1
    return x
print ("Complejidad O(log(n)) Logarithmic Time")
iterador_dividido(x)

import math
def iterador_incremento_exponencial(x:list) -> list: 
    iterador = len(x) 
    incremento = 1
    while(iterador > 0):
        iterador -= pow(incremento, 2)
        incremento += 1
    return x
print ("Complejidad O(log(log(n))) Logarithmic from Logarithmic Time")
iterador_incremento_exponencial(x)

y = list(np.random.randint(low=1,high=500000,size=999))

def calculo_bit_o_ejemplo(y:list) -> str: 
    iterador = -len(y) # k
    incremento = 1 # k
    q_list = y # k
    while(iterador < 0): # log(n)
        iterador /= incremento # k
        incremento += 1 # k
    for p in y: # n
        for q in y: # n -> n * n
            for r in y: # n -> n * n * n
                r
    return "La Complejidad es n*n*n, n cubo"
print ("Cálculo de la complejidad Algorítmica del Ejemplo")
calculo_bit_o_ejemplo(y)
