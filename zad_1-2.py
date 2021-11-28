from classes.Student import Student
from classes.Library import Library
from classes.Book import Book
from classes.Employee import Employee
from classes.Order import Order


student1 = Student('Adam', 99)
student2 = Student('Anna', 48)

print(student1.is_passed())
print(student2.is_passed())

lib1 = Library('Katowice', 'Mariacka', '41-100', '8-16', '598746502')
lib2 = Library('Bytom', 'Mariackowska', '41-500', '9-14', '591766100')
book1 = Book(lib1, '20.11.2021', 'Malysz', 'Adam', 999)
book2 = Book(lib1, '21.11.2021', 'Malysz', 'Adam', 99)
book3 = Book(lib1, '22.11.2021', 'Malysz', 'Adam', 9)
book4 = Book(lib2, '23.11.2021', 'Malysz', 'Adam', 9999)
book5 = Book(lib2, '28.11.2021', 'Malysz', 'Adam', 59)
employee1 = Employee('Anna', 'Kowalska', '12.02.2004',
                     '12.02.2004', '11.01.1990',
                     'Katowice', 'Mariacka', '41-100')
employee2 = Employee('Maria', 'Kowalska', '12.02.2004',
                     '12.02.2004', '11.01.1990',
                     'Katowice', 'Mariacka', '41-100')
employee3 = Employee('Katarzyna', 'Kowalska', '12.02.2004',
                     '12.02.2004', '11.01.1990', 'Katowice', 'Mariacka',
                     '41-100')
student1 = Student('Adam', 99)
student2 = Student('Anna', 99)
order1 = Order(employee1, student1, book1, '25.12.2021')
order2 = Order(employee2, student2, book2, '24.12.2021')

print(order1)
print(order2)
