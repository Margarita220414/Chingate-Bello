import csv
import json

wiht open ("customers.csv","r",) as elcsv:
    readercsv=csv.DictReader(elcsv)
    datacsv=[fila for fila in readercsv]
    print(readercsv)
    print(datacsv)
    
    