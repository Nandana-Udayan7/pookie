
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Salary(Employee):
    def __init__(self, name, emp_id, basic_pay, allowance):
        
        super().__init__(name, emp_id)
        self.basic_pay = basic_pay
        self.allowance = allowance

    def calculate_total_salary(self):
        return self.basic_pay + self.allowance

    def display_salary_details(self):
        self.display_info()
        total = self.calculate_total_salary()
        print(f"Basic Pay: {self.basic_pay}")
        print(f"Allowance: {self.allowance}")
        print(f"Total Salary: {total}")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_pay = float(input("Enter basic pay: "))
allowance = float(input("Enter allowance: "))

emp = Salary(name, emp_id, basic_pay, allowance)

emp.display_salary_details()





