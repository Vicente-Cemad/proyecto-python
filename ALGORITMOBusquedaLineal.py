from array import array

def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split(',')
        for line in lines:
            lista.append(line)
        return lista

def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    for actual in range(0, tamano_de_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    indice = lista.index(nombre_buscado)
    return indice

def main():
    lista_de_alumnos = sorted(importar_lista('archivo.txt'))
    print (lista_de_alumnos)
    posicion_del_alumno = buscar(lista_de_alumnos, "tres")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

if __name__ == "__main__":
    main()
