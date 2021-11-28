from zad_1 import Student


class Library:
    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka z miasta {self.city}, ul.: {self.street}, ' \
               f'kod pocztowy: {self.zip_code}. ' \
               f'Otwarta w godzinach: {self.open_hours}. ' \
               f'Telefon: {self.phone}'


class Order:
    def __init__(self, employee: str,
                 student: str, books: str, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie pracownika {self.employee}, ' \
               f'od studenta: {self.student}, ' \
               f'książka: {self.books}. ' \
               f'Data zamówienia: {self.order_date}'


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}. ' \
               f'Zatrudniony: {self.hire_date}. ' \
               f'Urodzony: {self.birth_date}. ' \
               f'Adres zamieszkania: {self.city}, ' \
               f'ul.: {self.street}, kod pocztowy: {self.zip_code}. ' \
               f'Telefon: {self.phone}'


class Book:
    def __init__(self, library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka z biblioteki {self.library}. ' \
               f'Data publikacji: {self.publication_date}. ' \
               f'Dane autora: {self.author_name} {self.author_surname}. ' \
               f'Liczba stron: {self.number_of_pages}'


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
