name = input('Your name: ')
lastname = input('Your lastname: ')
department = input('Name of your department: ')
year_of_entrance = input('The year of your entrance: ')
print()
class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name.title()
        self.lastname = lastname.title()
        self.department = department.title()
        self.year_of_entrance = year_of_entrance.title()

    def get_student_info(self):
        full_info = self.name + ' ' + self.lastname + ' enrolled at university to the department of ' + self.department + ' in ' + self.year_of_entrance + '.'
        return full_info

return_info = Student(name, lastname, department, year_of_entrance)
print(return_info.get_student_info())
print()
