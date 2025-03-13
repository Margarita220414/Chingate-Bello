import csv

# Función para cargar los datos desde el archivo CSV
def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Función para obtener el salario más alto y más bajo
def get_min_max_salary(data):
    salaries = [int(row['SALARY']) for row in data]
    return max(salaries), min(salaries)

# Función para agrupar por departamento
def group_by_department(data):
    departments = {}
    for row in data:
        dept_id = row['DEPARTMENT_ID']
        if dept_id not in departments:
            departments[dept_id] = []
        departments[dept_id].append(row)
    return departments

# Función para agrupar por manager
def group_by_manager(data):
    managers = {}
    for row in data:
        manager_id = row['MANAGER_ID']
        if manager_id not in managers:
            managers[manager_id] = []
        managers[manager_id].append(row)
    return managers

# Función para ordenar por apellido
def sort_by_last_name(data):
    return sorted(data, key=lambda x: x['LAST_NAME'])

# Función para ordenar por código de empleado
def sort_by_employee_id(data):
    return sorted(data, key=lambda x: int(x['EMPLOYEE_ID']))

# Cargar los datos
filename = 'employees.csv'
data = load_data(filename)

# Obtener salario más alto y más bajo
max_salary, min_salary = get_min_max_salary(data)
print(f"Salario más alto: {max_salary}")
print(f"Salario más bajo: {min_salary}")

# Agrupar por departamento
departments = group_by_department(data)
print("\nAgrupado por departamento:")
for dept_id, employees in departments.items():
    
    print(f"Departamento {dept_id}:")
    for emp in employees:
        print(emp)

# Agrupar por manager
managers = group_by_manager(data)
print("\nAgrupado por manager:")
for manager_id, employees in managers.items():
    print(f"Manager {manager_id}:")
    for emp in employees:
        print(emp)

# Ordenar por apellido
sorted_by_last_name = sort_by_last_name(data)
print("\nOrdenado por apellido:")
for emp in sorted_by_last_name:
    print(emp)

# Ordenar por código de empleado
sorted_by_employee_id = sort_by_employee_id(data)
print("\nOrdenado por código de empleado:")
for emp in sorted_by_employee_id:
    print(emp)
    
    