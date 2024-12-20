class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary= salary

    def get_salary(self):
        return self.__salary
    
    def display_info(self):
        print(f" Employee name is: {self.name}")
        #print(f" Salary or {self.name} is {self.__salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department= department
    
    def display_info(self):
        super().display_info()
        print(f"Department:{self.department}")

class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language

    def display_info(self):
        super().display_info()
        print(f"{self.name} uses {self.programming_language} for coding.")


manager_instance= Manager("Aditya Kashyap",40000000,"Data Science")
manager_instance.display_info()
#print("Salary is:", manager_instance.get_salary())

developer_instance= Developer("Ankita Ghosh",1200000,"Python")
developer_instance.display_info()
print(f"Salary is: {developer_instance.get_salary()}")

        
    
    

    