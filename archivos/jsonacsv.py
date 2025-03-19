import json
import csv

with open ("employees.json/employees.json","r",) as eljson:
    data=json.load(eljson)
    headers=data[0].keys()
    
    with open ("employees.json/empleados.csv","w") as elcsv:
        writer=csv.Dicwriter(elcsv,headers)
        writer.writeheader(data)