class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Nieruchomość o powierzchni (m^2): {self.area}, ' \
               f'liczbie pokoi: {self.rooms}, cenie: {self.price}, ' \
               f'i adresie: {self.address}. '


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int) -> object:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'{super().__str__()}Rozmiar działki m^2: {self.plot}. '


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'{super().__str__()}Piętro: {self.floor}. '


dom = House(115, 6, 1000000, 'Mariacka 1', 400)
mieszkanie = Flat(60, 3, 450000, 'Mickiewicza 25', 5)
print(dom)
print(mieszkanie)
