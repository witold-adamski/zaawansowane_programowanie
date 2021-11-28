class Produkt:
    def __init__(self, id: int, name: str, price: float, category_name: str,
                 category_id: int) -> None:
        self._id = id
        self._name = name
        self._price = price
        self._category_name = category_name
        self._category_id = category_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def category_name(self):
        return self._category_name

    @property
    def category_id(self):
        return self._category_id

    def __str__(self) -> str:
        return f'Nazwa produktu: {self._name}, ' \
               f'ID: {self._id}, ' \
               f'Cena: {self._price}, ' \
               f'Kategoria: {self._category_name}, ' \
               f'ID kategorii: {self._category_id}.'


class Magazyn:
    def __init__(self, id: int, name: str, country: str, street: str,
                 postal_code: str) -> None:
        self._id = id
        self._name = name
        self._country = country
        self._street = street
        self._postal_code = postal_code

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def street(self):
        return self._street

    @property
    def postal_code(self):
        return self._postal_code

    def __str__(self) -> str:
        return f'Nazwa magazynu: {self._name}, ' \
               f'ID: {self._id}, ' \
               f'Kraj: {self._country}, ' \
               f'Ulica: {self._street}, ' \
               f'Kod pocztowy: {self._postal_code}.'


class KlientDetaliczny:
    def __init__(self, id: int, name: str, surname: str,
                 country: str, street: str,
                 postal_code: str) -> None:
        self._id = id
        self._name = name
        self._surname = surname
        self._country = country
        self._street = street
        self._postal_code = postal_code

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def country(self):
        return self._country

    @property
    def street(self) -> str:
        return self._street

    @property
    def postal_code(self):
        return self._postal_code

    def __str__(self) -> str:
        return f'Imie: {self._name}, ' \
               f'Naziwsko: {self._surname}, ' \
               f'ID: {self._id}, ' \
               f'Kraj: {self._country}, ' \
               f'Ulica: {self._street}, ' \
               f'Kod pocztowy: {self._postal_code}.'


class Zamowienie:
    def __init__(self, id: int, quantity: int, country: str, street: str,
                 postal_code: str, product: Produkt, client,
                 magazyn: Magazyn) -> None:
        self._id = id
        self._quantity = quantity
        self._country = country
        self._street = street
        self._postal_code = postal_code
        self._product = product
        self._client = client
        self._magazyn = magazyn

    @property
    def id(self):
        return self._id

    @property
    def quantity(self):
        return self._quantity

    @property
    def country(self):
        return self._country

    @property
    def street(self):
        return self._street

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def product(self):
        return self._product

    @property
    def client(self):
        return self._client

    @property
    def magazyn(self):
        return self._magazyn

    @id.setter
    def id(self, value):
        self._id = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @country.setter
    def country(self, value):
        self._country = value

    @street.setter
    def street(self, value):
        self._street = value

    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value

    @product.setter
    def product(self, value):
        self._product = value

    @client.setter
    def client(self, value):
        self._client = value

    @magazyn.setter
    def magazyn(self, value):
        self._magazyn = value

    def __str__(self) -> str:
        return f'ID zamówienia: {self._id}, ' \
               f'Ilość: {self._quantity}, ' \
               f'Kraj: {self._country}, ' \
               f'Ulica: {self._street}, ' \
               f'Kod pocztowy: {self._postal_code},\n' \
               f'Produkt:\n {self._product},\n ' \
               f'Klient:\n {self.client}, \n' \
               f'Magazyn:\n {self.magazyn}'

    def total_price(self) -> float:
        return round(self.product.price*self.quantity, 2)

    def client_address(self) -> str:
       return f'Kraj: {self._country}, ' \
              f'Ulica: {self._street}, ' \
              f'Kod pocztowy: {self._postal_code}.'


class KlientBiznesowy(KlientDetaliczny):
    def __init__(self, id: int, name: str, surname: str,
                 country: str, street: str,
                 postal_code: str, nip: str) -> None:
        super().__init__(id, name, surname, country, street, postal_code)
        self._nip = nip

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def country(self):
        return self._country

    @property
    def street(self):
        return self._street

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def nip(self):
        return self._nip

    def __str__(self):
        return f'{super().__str__()}, ' \
               f'NIP: {self.nip}.'


produkt = Produkt(1, 'produkt1', 120, 'kategoria', 50)
magazyn = Magazyn(1, 'magazyn1', 'Polska', 'Mickiewicza', '41-100')
klient = KlientDetaliczny(1, 'Jan', 'kowalski', 'Polska', 'Słowackiego',
                          '40-100')
klientb2b = KlientBiznesowy(1, 'Adam', 'Malysz', 'Polska', 'Radosna',
                            '40-100', '1186924858')
zamowienie = Zamowienie(1, 10, 'Polska', 'Testowa', '40-200',
                        produkt, klient, magazyn)

print(produkt)
print(magazyn)
print(klient)
print(klientb2b)
print(zamowienie)
print(zamowienie.total_price())
print(zamowienie.client_address())


