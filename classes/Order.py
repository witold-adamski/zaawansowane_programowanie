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
