class Employee:
    id_counter = 1

    def __init__(self, name, salary):
        self.name = name
        self.employee_id = f"ED{Employee.id_counter:03}"
        self.salary = salary
        Employee.id_counter += 1  

    def display_details(self):
        print(f"\t{self.employee_id}\t\t\t{self.name}\t\t\t{self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to {self.salary} for employee {self.name}.")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to the department '{self.department_name}' with ID {employee.employee_id}.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for department '{self.department_name}': {total_salary}")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in the department '{self.department_name}':")
            print(f"\tEmployee ID\t\tFullName\t\tSalary(KSH)")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the department '{self.department_name}'.")


def main():
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\n\t\t\t\t\t\tEmployee and Department Management System.\nSelect an option amongst the following options below")
        print("\t\t1. Add an employee to the department")
        print("\t\t2. Display all employees in the department")
        print("\t\t3. Calculate and display total salary expenditure")
        print("\t\t4. Update employee salary")
        print("\t\t5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("\tEnter the employee's name: ")
            try:
                salary = float(input("\tEnter the employee's salary: "))
                employee = Employee(name, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid input. Salary must be a number")

        elif choice == '2':
            department.display_all_employees()

        elif choice == '3':
            department.calculate_total_salary_expenditure()

        elif choice == '4':
            employee_id = input("\n\nEnter the employee's ID: ")
            try:
                new_salary = float(input("Enter the new salary: "))
                employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)
                if employee:
                    employee.update_salary(new_salary)
                else:
                    print("Employee not found.")
            except ValueError:
                print("Invalid input. Salary must be a number.")

        elif choice == '5':
            print("\n\t\t\t\t\t\tExiting the management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
main()