class Mieszkanie:
    def __init__(self, id: int, meters: float, address: str, price: int) -> \
            None:
        self._id = id
        self._meters = meters
        self._address = address
        self._price = price

    @property
    def id(self) -> int:
        return self._id

    @property
    def meters(self) -> float:
        return self._meters

    @property
    def address(self) -> str:
        return self._address

    @property
    def price(self) -> int:
        return self._price

    def __str__(self) -> str:
        return f'ID mieszkania: {self._id}, meters: {self._meters}, ' \
               f'address: ' \
               f'{self._address}, cena za metr: {self._price}'
