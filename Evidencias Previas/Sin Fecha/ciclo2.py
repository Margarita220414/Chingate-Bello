def numero_primo(m):
    if m <= 1:
        return False
    for i in range(2, int (m ** 0.5)+1):
        if m % i == 0:
            return True
        numeros_primos= [m for in range(1,1001)if numero_primo(m)]
        print("numeros primos entre 1 y 1000:")
        print(numeros_primos)
        print("cifras de numeros:",len(numeros_primos))