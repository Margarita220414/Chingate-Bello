# ingrese un numero
def dividor(num):
    for i in range(1, num +1):
        if(num % i == 0):
            print(i,"es divisor de",num)
            print(f"{i} es divisor de {num}")

num = int(input("ingrese numero:"))
divisor(num)
divisor(10)
divisor(28)
