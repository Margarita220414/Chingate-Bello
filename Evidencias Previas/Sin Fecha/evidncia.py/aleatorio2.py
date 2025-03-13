import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def lista_sum(num1, num2):
    return (num1 + num2)
suma = 0
suma = lista_sum(5,20)
print(suma)

vec=[]
tam=random.randint(5,20)
vec=llenarListaRandom(vec,tam)
print(vec)
