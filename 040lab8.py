#Name Anns Khan
#Roll no 040


import csv

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID Number: {self.employee_id}, Post: {self.position}")

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Dept: {self.department}")

def read_employees_from_csv(filename):
    employees = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee = Staff(row['name'], int(row['age']), row['employee_id'], row['position'], row['department'])
            employees.append(employee)
    return employees

def add_employee(employees, name, age, employee_id, position, department):
    new_employee = Staff(name, age, employee_id, position, department)
    employees.append(new_employee)

def save_employees_to_csv(employees, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'age', 'employee_id', 'position', 'department']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow({'name': employee.name, 'age': employee.age, 'employee_id': employee.employee_id, 'position': employee.position, 'department': employee.department})

if __name__ == "__main__":
    employees = read_employees_from_csv("employees.csv")

    # Add new employees
    add_employee(employees, "Anns Khan", 20, "A09", "JAva", "Frontend")
    add_employee(employees, "Hamza", 21, "TG09", "Developer", "IT")

    # Display employee information
    for employee in employees:
        employee.display_info()
        employee.additional_info()
        print()

    # Save updated employee information
    save_employees_to_csv(employees, "employees.csv")