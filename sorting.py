from operator import itemgetter
from operator import attrgetter

employee_records = [ ('joe',1,53),('beck',2,26), \
                     ('ele',6,32),('neo',3,45),  \
                    ('christ',5,33),('trinity',4,29), \
                    ]

#Sorting by employee name
print sorted(employee_records, key = lambda emp: emp[0])

#Sorting by employee id
print sorted(employee_records, key = lambda emp: emp[1])

#Sorting by using itemgetter, attrgetter, and methodcaller functions
print sorted(employee_records, key = itemgetter(0))


class Employee(object):
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    
    def pretty_print(self):
        print self.name, self.id, self.age
    
employee_records = []

emp1 = Employee('joe', 1, 4)
emp2 = Employee('beck', 34, 23)
emp3 = Employee('ele', 5, 3)

employee_records.append(emp1)
employee_records.append(emp2)
employee_records.append(emp3)

employee_records_sorted = sorted(employee_records, key = attrgetter('age'))

for employee in employee_records_sorted:
    print employee.pretty_print()