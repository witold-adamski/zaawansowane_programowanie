from classes.Property import Property


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'{super().__str__()}Rozmiar działki m^2: {self.plot}.'
