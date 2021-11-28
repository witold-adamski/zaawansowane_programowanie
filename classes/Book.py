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
