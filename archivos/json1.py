import json 

with open ("employees.json","r",) as salario:
    lista_1 = json.load(salario)
print(lista_1)
lista_2=[]
for i in lista_1:
    print(i["SALARY"])
    print("-"*30)
    lista_2.append(salario)
    #print(lista_2)
    def promedio():
    return sum(lista_2) / len(lista_2)
    print (promedio)
    
    
    newdata={
         "EMPLOYEE_ID": "500",
        "FIRST_NAME": "geremias",
        "LAST_NAME": "Springfin",
        "EMAIL": "GER@1234",
        "PHONE_NUMBER": "123.507.890",
        "HIRE_DATE": "22-ABRIL-2014",
        "JOB_ID": "SH_CLERK",
        "SALARY": "3000",
        "COMMISSION_PCT": " - ",
        "MANAGER_ID": "124",
        "DEPARTMENT_ID": "40"
         
    }
    
    lista_2.append(newdata)
    with open ("employees.json","w",) as salario:
        json.dump(lista_2,salario)
        
        usuario=int(input("digite un numero: "))
        print(usuario)
        
    lista_2.append(usuario)
    print(lista_2)
        
        