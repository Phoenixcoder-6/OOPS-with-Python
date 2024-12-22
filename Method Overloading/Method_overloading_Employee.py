class Employee:
    def get_details(self, name= None, age= None, department= None):
        if name is None and age is None and department is None:
            return f" No details available."
        elif age is None and department is None:
            return f"Name: {name}"
        elif department is None:
            return f"Name:{name}, Age:{age}"
        else:
            return f"Name:{name}, Age:{age}, Department:{department}"
        

emp=Employee()
print(emp.get_details())
print(emp.get_details("Dean"))
print(emp.get_details("Dean",29))
print(emp.get_details("Dean",29,"Hunter"))
        

        