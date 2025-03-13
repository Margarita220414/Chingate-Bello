import random

aleatorio1 = random.randint(100)
aleatorio2 = random.randint(10,20)
print(f"aleatorio1={aleatorio1}")
print(f"aleatorio2={aleatorio2}")


for num in range(10):
    aleatorio1 = random.randint(1,100)
aleatorio2 = random.randint(10,20)
print(f"aleatorio1={aleatorio1}")
print(f"aleatorio2={aleatorio2}")



import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
tam=int(input("Cuantos numeros ingreso a la lista"))
vec=llenarListaRandom(vec,tam)
print(vec)