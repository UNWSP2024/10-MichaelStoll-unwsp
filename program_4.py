#title:employee class
#author: michael stoll
#date:3/31/2025
class Employee:

    def __init__(self, name, id_number, department, job):
        self.name = name
        self.id = id_number
        self.department = department
        self.job = job

employee1 = Employee('Susan Meyers',47899,'Accounting','Vice President')
employee2 = Employee('Mark Jones',39119,'IT','Programmer')
employee3 = Employee('Joy Rogers',81774,'Manufacturing','Engineer')

print(employee1.name, employee1.id, employee1.department, employee1.job)
print(employee2.name, employee2.id, employee2.department, employee2.job)
print(employee3.name, employee3.id, employee3.department, employee3.job)