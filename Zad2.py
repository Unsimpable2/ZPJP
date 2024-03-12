class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, {self.publication_date}, {self.number_of_pages}, {self.library}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = '\n\t\t'.join([str(book) for book in self.books])
        return f"Order:\n\tEmployee: {self.employee}\n\tStudent: {self.student}\n\tBooks: \n\t\t{book_list}\n\tOrder Date: {self.order_date}"

library1 = Library("Sworne Gacie", "Ratusz", "42069", "8 - 18", "888-888-888")
library2 = Library("Zimna Wodka", "Wodki", "21370", "7 - 18", "999-999-999")

book1 = Book(library1, "23 01 2012", "Dawid", "Jackowski", 100)
book2 = Book(library1, "18 03 2001", "Marta", "Kowalska", 120)
book3 = Book(library1, "20 08 2022", "Michal", "Sikora", 140)
book4 = Book(library2, "02 01 2024", "Lukasz", "Ulkowski", 160)
book5 = Book(library2, "30 10 1990", "Natalia", "Pstrag", 200)

employee1 = Employee("Magdalena", "Poniatowska", "10 02 2018", "20 05 2000", "Sworne Gacie", "Adamczyka", "42069", "111-111-111")
employee2 = Employee("Ewa", "Michalczyk", "22 11 2009", "2512 1985", "Zimna Wodka", "Czwartkowa", "21370", "333-333-333")
employee3 = Employee("Adam", "Piotrkowski", "10 10 2020", "21 02 2001", "Sworne Gacie", "Gwiazdowa", "42069", "222-222-222")

order1 = Order(employee1, "Witold", [book1, book2], "11 02 2024")
order2 = Order(employee2, "Natalia", [book3, book4, book5], "09 03 2024")

print(order1)
print("\n")
print(order2)