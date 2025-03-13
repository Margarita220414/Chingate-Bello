print("digite tres numeros:")
num1 = int(input("digite el primer numero:"))
num2 = int(input("digite el segundo numero:"))
num3 = int(input("digite el tercer numero:"))
mayor = max (num1,num2,num3)
menor = min (num1,num2,num3)
valor_medio = (num1+num2+num3) - menor - mayor
print("el valor medio es:")
print(valor_medio)