import csv
with open ("employees.csv","r") as empleados:
    data = csv.reader(empleados)
    
    for x in data:
        print(x[1])
        print(x[2])
        print(x[7])
        empleados= [for x in data.radines,empleados.strip(),empleados.split(",")]
print(type(data))
lista=list(data[])
print(type(lista)) 
print(len(lista))
lista.pop(0)
salarios=[]
for emp in lista:
    salarios.appped(int(emp[7]))
         
sal_mayor= max(empleados.keys())
sal_menor= min(empleados.keys())
persona_max= [nombre for nombre, salario in datos in datos.items() if salario= sal_mayor[0]]
persona_min= [nombre for nombre, salario in datos in datos.items() if salario= sal_menor{0}]
  
print(f"el salario más alto es de {sal_mayor}.")
print(f"el salario más alto es de {sal_menor}.")
