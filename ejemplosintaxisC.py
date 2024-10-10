import math

print (math.pi * 4)
# 12.566370614359172

print (math.pi ** 2)
# 9.869604401089358

print (math.sqrt(4)) # Raíz cuadrada
# 2

print (math. sqrt(12))
# 3.4641016151377544

import random

print (random.random ())
# 0.6567888091274212 -> cambia de valor

lista = [1, 2, 3, 4]
print (random.choice(lista))
# 3 -> cambia de valor

random.shuffle(lista)
print (lista)
# [2, 3, 1, 4] -> NO cambia de valor
