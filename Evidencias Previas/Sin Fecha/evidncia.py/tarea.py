def lista_sum(num1, num2, num3):
    return (num1 + num2+ num3 )
suma = 0
suma = lista_sum(4,20,10)
print(suma)

def lista_pro(num1, num2, num3):
    return (num1 + num2+ num3 )/3
suma = 0
promedio = lista_pro(4,20,10)
print(promedio)

lista_mayor=[4,20,10]
mayor = max(lista_mayor)
print(mayor)

lista_menor=[4,20,10]
menor = min(lista_menor)
print(menor)

lista_mediana= [4,20,10]
mediana = (4+20+10)/2
print(mediana)

lista = [4,20,10]
media = (4+20+10)/2
varianza = float(2-media**2 + 20-media**2 + 8-media**2)/2
print(varianza)

import math


def des_estandar (num1, num2,num3):
    media = (num1+num2+num3)/2
    varianza = (num1-media**2 + num2-media**2 + num3-media**2)/2
    return math.sqrt(varianza)
print(des_estandar)
