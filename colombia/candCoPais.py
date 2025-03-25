import csv
from collections import Counter

with open('colomdata.csv', newline='', encoding='utf-8') as ciudad:
    readercsv=csv.DictReader(ciudad)
    ciudadN=[x["Ciudad de Nacimiento"].split('-')[0] for x in readercsv if x["Ciudad de Nacimiento"]]
    colombianos = [m for m in ciudadN if "COLOMBIA" in m]
    frecu_colom = Counter( colombianos )
    print(frecu_colom)
    for Ciudad, frecuencia in frecu_colom.items():
        print(f"{Ciudad}: {frecuencia} colombianos")
    can_col=len(colombianos)
    print("la cantidad de colombianos en todos los paises es de:",can_col)
    
    