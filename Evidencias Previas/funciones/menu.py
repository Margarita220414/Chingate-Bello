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

vec =[]
tam=random.randint(5,20)
vec=llenarlista(vec,tam)
print(vec)
print(sumalista(vec))


def llenarlista(lista,cantidad):
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append(num)
    return lista


def prolista(lista):
    suma = 0
    for i in lista:
        suma += i
    return  suma / tam

vec =[]
tam=random.randint(5,20)
vec=llenarlista(vec,tam)
print(vec)
print(prolista(vec))


def llenarlistarandom(lista, cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append (num)
    return lista 

def mayorlista(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    return f" el mayor es {mayor}"

vec =[]
tam=random.randint(5,20)
vec= llenarlistarandom(vec,tam)
print(vec)
print(mayorlista(vec)) 



def llenarlistarandom(lista, cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append (num)
    return lista 

def menorlista(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return f" el menor es {menor}"

vec =[]
tam=random.randint(5,20)
vec= llenarlistarandom(vec,tam)
print(vec)
print(menorlista(vec)) 


def llenarlistarandom(lista, cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append (num)
    return lista 

def ascendentelista(lista):
    ascendente = lista[0]
    return f" el ascendente es {ascendente}"

vec =[]
tam=random.randint(5,20)
vec= llenarlistarandom(vec,tam)
print(vec)
print(ascendentelista(vec)) 



def llenarlistarandom(lista, cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append (num)
    return lista 

def descendentelista(lista):
    descendente = lista[0]
    return f" el descendente es {descendente}"

vec =[]
tam=random.randint(5,20)
vec= llenarlistarandom(vec,tam)
print(vec)
print(descendentelista(vec)) 


def llenarlistarandom(lista, cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append (num)
    return lista 

def medianalista(lista):
    mediana = lista[0]
    return f" el mediana es {mediana}"

vec =[]
tam=random.randint(5,20)
vec= llenarlistarandom(vec,tam)
print(vec)
print(medianalista(vec)) 

sel=1
while sel != 9:
    
    print("1-sumalista")
    print("2-prolista")
    print("3-mayorlista")
    print("4-menorlista")
    print("5-ascendentelista")
    print("6-desendentelista")
    print("7-medianalista")
    print("8-salir")
    sel= int(input("seleccione opcion: "))
    
    
    match sel !=9:
        case 1:
            print(sumalista(vec))
        case 2: 
            print(prolista(vec))
        case 3: 
            print(mayorlista(vec))
        case 4: 
            print(menorlista(vec)) 
        case 5: 
            print(ascendentelista(vec)) 
        case 6: 
            print(descendentelista(vec)) 
        case 7: 
            print(ascendentelista(vec))
        case 8: 
            print(medianalista(vec))
        case 9:
            print("opcion equivocada")
        