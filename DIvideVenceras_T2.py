import random


def crear_palabra():
    return ''.join(chr(random.randint(97, 122)) for _ in range(4))


def crear_matriz(tamano):
    return [[crear_palabra() for _ in range(tamano)] for _ in range(tamano)]


def tiene_vocal(palabra):
    for letra in palabra:
        if letra in 'aeiou':
            return True
    return False


def contar_vocales_matriz(matriz):
    n = len(matriz)
    if n == 1:
        return 1 if tiene_vocal(matriz[0][0]) else 0
    mitad = n // 2
    arriba_izq = [fila[:mitad] for fila in matriz[:mitad]]
    arriba_der = [fila[mitad:] for fila in matriz[:mitad]]
    abajo_izq = [fila[:mitad] for fila in matriz[mitad:]]
    abajo_der = [fila[mitad:] for fila in matriz[mitad:]]
    return (contar_vocales_matriz(arriba_izq) +
            contar_vocales_matriz(arriba_der) +
            contar_vocales_matriz(abajo_izq) +
            contar_vocales_matriz(abajo_der))


tamano = int(input("Tamaño de la matriz: "))
matriz = crear_matriz(tamano)

for fila in matriz:
    print(' '.join(fila))

total = contar_vocales_matriz(matriz)
print(f"Total de palabras con al menos una vocal: {total}")
