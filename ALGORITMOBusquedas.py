#BÚSQUEDAS LINEALES
from array import array

def buscar(lista, nombre_buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    return -1
def main():
    #lista_de_alumnos = sorted(importa_lista('../data/lista_alumnos'))
    lista_de_alumnos = sorted(importa_lista[:])
    #posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
    posicion_del_alumno = buscar(lista_de_alumnos, "dos")
    print (lista_de_alumnos)
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

importa_lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print (importa_lista)
if __name__ == "__main__":
    main()
    
def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista

def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    for actual in range(0, tamano_de_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    return -1
def main():
    #lista_de_alumnos = sorted(importa_lista('../data/lista_alunos'))
    #posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
    lista_de_alumnos = sorted(importar_lista('archivo.txt'))
    print (importar_lista('archivo.txt'))
    posicion_del_alumno = buscar(lista_de_alumnos, "dos")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))
    print (lista_de_alumnos)

if __name__ == "__main__":
    main()

from array import array

def buscar(lista, nombre_buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    return -1
def main():
    #lista_de_alumnos = sorted(importa_lista('../data/lista_alumnos'))
    #posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
    #bucle solo suma tiempo y consumo, sin logica añadida
    #for i in range(0, 3500):
        lista_de_alumnos = sorted(importa_lista[:])
        posicion_del_alumno = buscar(lista_de_alumnos, "dos")
        print (lista_de_alumnos)
        print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

importa_lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print (importa_lista)
if __name__ == "__main__":
    main()

#BÚSQUEDAS BINARIAS
from array import array

def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
        
    for line in lines:
        print (lines)
        lista.append(lines)
    print(lista)
    return lista

def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    inicio = 0
    fin=tamano_de_lista-1
    while inicio<=fin:
        medio=(inicio+fin)//2
        if lista[medio] == nombre_buscado:
            return medio
        elif lista[medio] < nombre_buscado:
            inicio=medio+1
        elif lista[medio] > nombre_buscado:
            fin = medio-1
    return -1

def main():
    #lista_de_alumnos = sorted(importar_lista('../data/lista_alumnos'))
    #lista_de_alumnos = sorted(importar_lista('archivo.txt'))
    lista_sin = importar_lista('archivo.txt')
    print (lista_sin)
    #lista_de_alumnos = sorted(importar_lista('archivo.txt'))
    lista_de_alumnos = sorted(lista_sin)
    print (lista_de_alumnos)
    #for i in range(0,3500):
        #posicion_del_alumno = buscar(lista_de_alumnos, "Zoraida")
    posicion_del_alumno = buscar(lista_de_alumnos, "tres")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

if __name__ == "__main__":
    main()
