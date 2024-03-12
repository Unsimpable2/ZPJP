class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: Area - {self.area} sqm, Rooms - {self.rooms}, Price - ${self.price}, Address - {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: Area - {self.area} m2, Rooms - {self.rooms}, Price - zl {self.price}, Address - {self.address}, Plot - {self.plot} m2"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: Area - {self.area} m2, Rooms - {self.rooms}, Price - zl {self.price}, Address - {self.address}, Floor - {self.floor}"

house1 = House(200, 7, 1200000, "Katowice Stawowa 23", 450)
flat1 = Flat(80, 4, 520000, "Gliwice Piwna 3", 2)

print(house1)
print(flat1)