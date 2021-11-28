from classes.Property import Property


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'{super().__str__()}Piętro: {self.floor}. '
