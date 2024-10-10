'''
Crea una función log que acepte cualquier número de 
argumentos y los imprima por pantalla en una misma 
línea. La línea debe empezar con el prefijo ‘LOG: ’.
Modifica la función log para que usuario pueda 
especificar cualquier prefijo que desee.
Modifica la función log para que el prefijo tenga el 
valor por defecto ‘LOG: ’.
Modifica la función log para que el usuario pueda 
establecer tanto prefijo como separador entre 
argumentos. Ambos deben pasarse sólo por los 
nombres (no por posición) ‘sep’ y ‘prefix’. No hace 
falta que estos tengan valor por defecto.
Modfica la función log para que ahora ‘sep’ y ‘prefix’ 
tengan un valor por defecto.
Modifica la función log para que acepte el siguiente 
diccionario. Recuerda que hay que pasarlo 
desempaquetándolo con la sintaxis de doble 
asterisco (**)
'''

#1
def log(*args):
    print('LOG:', *args)

log('mensaje', 'de', 'prueba')  # Salida: LOG: mensaje de prueba

#2
def log(prefix, *args):
    print(prefix, *args)

log('INFO:', 'mensaje', 'de', 'prueba')  # Salida: INFO: mensaje de prueba

#3
def log(*args, prefix='LOG:'):
    print(prefix, *args)

log('mensaje', 'de', 'prueba')  # Salida: LOG: mensaje de prueba
log('mensaje', 'de', 'prueba', prefix='INFO:')  # Salida: INFO: mensaje de prueba

#4
def log(*args, sep=' ', prefix='LOG:'):
    print(prefix, sep.join(map(str, args)))

log('mensaje', 'de', 'prueba')  # Salida: LOG: mensaje de prueba
log('mensaje', 'de', 'prueba', prefix='INFO:', sep=' - ')  # Salida: INFO: mensaje - de - prueba

#5
def log(*args, sep=' ', prefix='LOG:'):
    print(prefix, sep.join(map(str, args)))

log('mensaje', 'de', 'prueba')  # Salida: LOG: mensaje de prueba
log('mensaje', 'de', 'prueba', prefix='INFO:', sep=' - ')  # Salida: INFO: mensaje - de - prueba

#6
def log(*args, sep=' ', prefix='LOG:'):
    print(prefix, sep.join(map(str, args)))

# Diccionario de ejemplo
params = {'sep': ' - ', 'prefix': 'DEBUG:'}
log('mensaje', 'de', 'prueba', **params)  # Salida: DEBUG: mensaje - de - prueba

def f(**kargs): # Acepta número de argumentos
    print (kargs)
    
kargs = {'a': 1}
f(**kargs)
kargs = {'a': 1, 'b': 2}
f(**kargs)
kargs = {'a': 1, 'c': 3, 'b': 2}
f(**kargs)
