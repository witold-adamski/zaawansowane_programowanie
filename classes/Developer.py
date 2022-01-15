class Developer:
    def __init__(self, id: int, name: str, address: str, nip: str) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._nip = nip

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> str:
        return self._address

    @property
    def nip(self) -> str:
        return self._nip

    def __str__(self) -> str:
        return f'ID: {self._id}, name: {self._name}, address: ' \
               f'{self._address}, nip: {self._nip}'
