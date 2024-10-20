from math import pi

def area(r):
#Verificamos los tipos correctos
    if type(r) not in [float, int]:
        print ('BIEN, NI FLOTANTES NI INTEGER')
        raise TypeError("Solo números enteros o de coma flotante.")

    if r<0:
        print ('BIEN, NEGATIVOS')
        raise ValueError("No se permiten valores negativos")
    areaC = pi*(r**2)
    print ('BIEN')
    return areaC
