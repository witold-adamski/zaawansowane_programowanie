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
