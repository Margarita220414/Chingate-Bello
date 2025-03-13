def llenarlista(lista,cantidad):
    lista =[]
    num=0
    for i in range(cantidad):
        num=int(input("ingrese numero"))
        lista.append(num)
        lista.append(i*10)
        return lista
    
    
    
