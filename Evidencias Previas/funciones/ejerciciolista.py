def media(lista):
    suma = 0
    for n in lista:
        suma += n
    return  suma / len(lista)

def rebanadas(lista,ini,fin):
    if ini>len(lista) or fin<len(lista)*-1: #pregunta por los limites negativos
        return "fuera del rango de la lista"
    else:
        return lista[ini:fin]

def mitades(lista):
    tam=len(lista)
    print(tam)
    if tam%2!=0:
        m=media(lista)
        lista.append(int(m))
        print(lista)
        r1=lista[:int(tam/2)]
        r2=lista[int(tam/2):]
        print(f"mitad1= {r1}")
        print(f"mitad2= {r2}")

import random
def llenarlistaRandom(lista):
    lista=[]
    cantidad=random.randint(5,20)
    num=0
    for i in range(cantidad):
        num=random.randint(1, 100)
        lista.append(num)
    return lista

vector =[]
vector=llenarlistaRandom(2,4)
print(vector)
reb1=rebanadas(vector,2,4)
mitades(vector)