def impri_figura(lineas):
    for i in range(1,lineas+1):
        for j in range(1,lineas+1):
            print("*", end="")
            lineas = int(input("ingrese el numero de lineas que desea imprimir:"))
            impri_figura(lineas)