import csv
with open('registros.csv', 'r') as elcsv:
    data=csv.reader(elcsv)
    
    print(type(data))
    for i in data:
        print(i['])
        print("-"*30)
    print(data)
    
    