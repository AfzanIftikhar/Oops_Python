# ------------------------ Employee Management System ----------------------

class Employee:
    def __init__(self, name,employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        return f"Name : {self.name} \t  Id : {self.employee_id}, \t Salary : {self.salary}"

    def calculate_salary(self):
       
        return  self.salary 

    # def __add__(self,other):

    #     sum = 0
    #     for i in other:
    #         sum = sum + i.salary

    #     return f"Sum of salaries are {self.salary + sum}"


class Developer(Employee):
    def __init__(self, name, employee_id, salary,programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
        
    def write_code(self):
        return f"{self.name} writes code in {self.programming_language} programming language."

    def calculate_salary(self):
        return f"Total salary is : {super().calculate_salary()}"

class Manager(Employee):
    def __init__(self,name,employee_id,salary,team_size):
        super().__init__(name,employee_id,salary)
        self.team_size = team_size

    def conduct_meeting(self):
        return f"{self.name} is conducting meeting with team of {self.team_size}  "

    def calculate_salary(self):
        return f"Total salary is {super().calculate_salary() + 1000}"


class Designer(Employee):
    def __init__(self, name, employee_id, salary, design_tool):
        super().__init__(name, employee_id, salary)
        self.design_tool = design_tool

    def create_design(self):
        return f"{self.name} is creating a design with {self.design_tool}"

    def calculate_salary(self):
        return f"Total salary is : {super().calculate_salary()}"
    

obj = Employee("Afzan", 1 , 23000)
obj1 = Employee("Qasim", 2 , 21000)
obj2 = Employee("Muhtasib", 3 , 22000)
obj3 = Employee("Muhtasib", 3 , 22000)
obj4 = Employee("Zaid", 4 , 23000)

dev = Developer("Afzan Khan", 5, 50000,"python")
manager = Manager("Syed Muhammad Qasim ", 6, 80000, 7)
designer = Designer("Syed Muhtasib Shah" , 7, 40000, "Canva")


print(dev.display_details())
print(dev.write_code())
print(dev.calculate_salary())

print("-------------------------------------------------------")

print(manager.display_details())
print(manager.conduct_meeting())
print(manager.calculate_salary())

print("-------------------------------------------------------")

print(designer.display_details())
print(designer.create_design())
print(designer.calculate_salary())

print("-------------------------------------------------------")


        