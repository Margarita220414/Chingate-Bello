#crear paquetes en python
import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def mayorLista(lista):
    mayor = lista[0]
    sum=0
    # for i in range(len(lista)):
    #     sum+=lista[i]
    for x in lista:
        if x > mayor:
            mayor = x
    return f"el numero mayor es:{mayor}"

vector=[]
tam=random.randint(5,20)
vector=llenarListaRandom(vector,tam)
print(vector)
print(mayorLista(vector))