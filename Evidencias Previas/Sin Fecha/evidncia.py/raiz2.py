import math
def validar(a,b,c):
    calcular = b**2 - 4**a*c
    if calcular < 0:
        print("solucion")
    elif calcular == 0:
        x = -b / (2*a)
        
math.sqrt