def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 10)
except IndexError: #Captura Indexerror
    print(IndexError)
    print(indexador)
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')

def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 'h')
except (IndexError, TypeError): # Captura varios errores
    print('Error.')
print('Hemos salido del try-catch')

try:
    indexador('Python', 'h')
except: # Captura todos los errores. No recomendado.
    print('Error.')
print('Hemos salido del try-catch')

def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 'h')
except IndexError: # Captura 
    IndexError
    print('Error de índice.')
except TypeError: # Captura 
    print (TypeError)
    print('El índice tiene que ser un número.')
print('Hemos salido del try-catch')

try:
    raise IndexError('Excepción lanzada manualmente')
except:
    print('He capturado mi pripia excepción')

a = 10
b = 0
assert(a > b), 'A tiene que ser mayor que B!' # Si se cumple no salta el error
print('Si se muestra esto es que no ha saltado el assert')

'''
Recomendado en el desarrollo durante las pruebas, pero no en producción
a = 10
b = 0
c = 5
assert(a == c), 'A y C tienen que ser iguales!'
'''

class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    pass

try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print('He capturado mi propia excepción')

class miError(Exception):

    def __init__(self, valor):
        self.valor = valor
        print(miError)
    def __str__(self):
        print(miError)
        return str(self.valor)


try:
    raise miError("error o no")
except miError as e:
    print(f'He capturado mi propia excepción {e}')

def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 10)
except IndexError as e:
    print(f"Se produjo una excepción: {e}")
'''
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
'''
print('Este print también se ejecuta')

def divide(x, y):

    try:
        resultado = x/y
        print('El resultado es: {a}'.format(a=resultado)) #Se lo salta si da error
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: {a}'.format(a=resultado))
    finally:
        print('Con o sin error: Ejecutamos el finally')

divide(4, 12) #Sin error
divide(4, 0) #Con error
