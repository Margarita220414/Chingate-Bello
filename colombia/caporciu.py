import csv
from collections import Counter

with open('colomdata.csv', newline='', encoding='utf-8') as ciudadDR:
    readercsv=csv.DictReader(ciudadDR)
    ciudadRE=[x["Ciudad de Residencia"].split('-')[0] for x in readercsv if x["Ciudad de Residencia"]]
    frecu_colom = Counter(ciudadRE)
    print(frecu_colom)
    for CiudadDr, frecuencia in frecu_colom.items():
        print(f"{CiudadDr}: {frecuencia} cantidad de personas por ciudades")