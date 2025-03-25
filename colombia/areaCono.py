import csv
from collections import Counter

with open('colomdata.csv', newline='', encoding='utf-8') as areCo:
    readercsv=csv.DictReader(areCo)
    area=[x["Área Conocimiento"].split('-')[0] for x in readercsv if x["Área Conocimiento"]]
    frecu_areas= Counter(area)
    print(frecu_areas)
    for Ciudad, frecuencia in frecu_areas.items():
        print(f"{Ciudad}: {frecuencia} areas de conocimiento")