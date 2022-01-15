from classes.Developer import Developer


class Zamowienie:
    def __init__(self, id: int, developer: Developer, flats_list: list,
                 name: str) -> None:
        self._id = id
        self._developer = developer
        self._flats_list = flats_list
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, value: Developer) -> None:
        self._developer = value

    @property
    def flats_list(self) -> list:
        return self._flats_list

    @flats_list.setter
    def flats_list(self, value: list) -> None:
        self._flats_list = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def id(self, value: str) -> None:
        self._name = value

    def __str__(self) -> str:
        return f'ID zamowienia: {self._id}, deweloper: ' \
               f'{self._developer.name}, ' \
               f'adresy mieszkań/domów: ' \
               f'{[x.address for x in self._flats_list]}, nazwa osiedla:' \
               f' {self._name}, cena całkowita: {self.price()}, ' \
               f'suma metrów: {self.meters_sum()}.'

    def price(self) -> float:
        suma = 0
        for flat in self._flats_list:
            suma += flat.price*flat.meters
        return round(suma, 2)

    def meters_sum(self) -> float:
        suma = 0
        for flat in self._flats_list:
            suma += flat.meters
        return suma
