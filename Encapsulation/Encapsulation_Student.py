class Student:
    def __init__(self, name, grade):
        self.__name=name
        self.__grade= grade

    def get_name(self):
        return self.__name
    def set_name(self,name):
        if name.strip():
            self.__name=name
        else:
            print("Name cannot be empty.")
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("Grade must be between 0 to 100.")

    def display_info(self):
        print(f"Student's Name: {self.__name}")
        print(f"Student's Grade: {self.__grade}")


student_instance= Student("Ankita Ghosh",89)
student_instance.display_info()

student_instance.set_name("Soumya Ghosh")
student_instance.set_grade(92)
student_instance.display_info()
