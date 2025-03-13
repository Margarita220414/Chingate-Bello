def rango(ni,nf):
    if ni<nf:
        while ni<nf:
            if ni%7==0:
                print(f"{ni} factor de 7")
            else:
                print(ni)
            ni+=1
        
        else:
            print("Ciclo ascendente finalizado")
            print("Desde else en el while")
    elif ni>nf:
        while ni>nf:
            print(ni)
            ni-=1
        else:
            print("Ciclo descendente finalizado")
            print("Desde else en el while")

rango(7,30)