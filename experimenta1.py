


print (10/3)
print (10//3)
print (10)
print (10/2)
print (9)
print (9/2)
print (8)
print (8/2)
print (7)
print (7/2)
print (6)
print (6/2)
print (5)
print (5/2)
print (4)
print (4/2)
print (3)
print (3/2)
print (2)
print (2/2)
print (1)
print (1/2)

lista1 = []
lista2 = []
x=10
while x > 1 :
    if x / 2 == x // 2 :
       print ('true')
       print (x)
       print (x / 2)
       lista1.append(x)
       x = x - 1
    else :
       print ('false')
       print (x)
       print (x / 2)
       lista2.append(x)
       x = x - 1
print (lista1)
print (lista2)

lista1 = []
lista2 = []
lista3 = []
x=10
while x > 1 :
    if x / 2 == x // 2 :
        if x / 3 == x // 3 :
            lista1.append (x)
            x = x - 1
        else :
            lista2.append (x)
            x = x - 1
    else :
        lista3.append (x)
        x = x - 1
print (lista1)
print (lista2)
print (lista3)

def criba_eratostenes(n):
    # Crear una lista de booleanos que representa si cada número es primo
    primos = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        # Si primos[p] no ha sido cambiado, entonces es un número primo
        if (primos[p] == True):
            # Actualizar todos los múltiplos de p como no primos
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    # Recoger todos los números primos
    return [p for p in range(2, n) if primos[p]]

# Ejemplo de uso
n = 100
print(f"Números primos menores que {n}: {criba_eratostenes(n)}")

def descomponer_factores(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores

# Ejemplo de uso
numero = 100
print(f"Los factores primos de {numero} son: {descomponer_factores(numero)}")
