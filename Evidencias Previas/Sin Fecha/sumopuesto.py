def sum_opuesto():
    num = 1
    sum = 0
while num!=0:
    num=int(input("ingrese el numero"))
    print(num*+1)
    sum = sum + num
    c=c+1
    
    
    return sum,c-1
print(f"imprimir la suma de los numeros y la cantidades {sum_opuesto()}")