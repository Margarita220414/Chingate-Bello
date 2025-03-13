def rango(ni,nf):
    if ni<nf:
        while ni<nf:
            print(ni)
            ni+=1
        else:
            print("Ciclo de finalizado")
            print("Desde else en el while")
            
    elif ni>nf:
        if ni<nf:
            while ni>nf:
                print(ni)
                ni+=1
        else:
            print("Ciclo de finalizado")
            print("Desde else en el while")

rango(1,15)