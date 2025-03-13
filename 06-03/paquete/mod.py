from mod import sumalista, prolista, mayorlista, menorlista, ascendentelista, descendentelista, medianalista


import random

def llenarlista(lista,cantidad):
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append(num)
    return lista

def sumalista(lista):
    suma = 0
    for i in lista:
        suma += i
    return  suma

def prolista(lista):
    suma = 0
    for i in lista:
        suma += i
    return  suma / len(lista)

def mayorlista(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    return f" el mayor es {mayor}"

def menorlista(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return f" el menor es {menor}"

def ascendentelista(lista):
    ascendente = lista[0]
    return f" el ascendente es {ascendente}"

def descendentelista(lista):
    descendente = lista[0]
    return f" el descendente es {descendente}"

def medianalista(lista):
    mediana = lista[0]
    return f" el mediana es {mediana}"

vec = []
tam=random.randint(5,20)
vec=llenarlista(vec,tam)
print(vec)
print(sumalista(llenarlista), prolista(llenarlista), mayorlista(llenarlista), menorlista(llenarlista), ascendentelista(llenarlista), descendentelista(llenarlista), medianalista(llenarlista))