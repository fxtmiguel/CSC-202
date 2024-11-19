class Flower:

    # Common base class for all Flowers

    def __init__(self, petalName, petalNumber, petalPrice):
        self.name = petalName

        self.petals = petalNumber

        self.price = petalPrice

    def setName(self, petalName):
        self.name = petalName

    def setPetals(self, petalNumber):
        self.petals = petalNumber

    def setPrice(self, petalPrice):
        self.price = petalPrice

    def getName(self):
        return self.name

    def getPetals(self):
        return self.petals

    def getPrice(self):
        return self.price


# This would create first object of Flower class

f1 = Flower("Sunflower", 2, 1000)

print("Flower Details:")
print("Name: ", f1.getName())
print("Number of petals:", f1.getPetals())
print("Price:", f1.getPrice())
print("\n")

# This would create second object of Flower class

f2 = Flower("Rose", 5, 2000)
f2.setPrice(3333)
f2.setPetals(6)
print("Flower Details:")
print("Name: ", f2.getName())
print("Number of petals:", f2.getPetals())
print("Price:", f2.getPrice())
print("\n")


class Product:
    def __init__(self, product, amount, price):
        self.name = product
        self.amount = amount
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        self.amount = amount

    def set_price(self, price):
        self.price = price

    def get_price(self, item_amount):
        regular_price = self.price * item_amount
        discount = 0

        if item_amount > 9:
            discount = 0.1
            if item_amount > 99:
                discount = 0.2

        return regular_price - (regular_price * discount)

    def make_purchase(self, item_amount):
        item_amount -= self.amount
        return item_amount 


class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def inches(self):
        if self.unit == 'inches':
            return self.length
        elif self.unit == 'feet':
            return self.length * 12
        elif self.unit == 'yards':
            return self.length * 36
        elif self.unit == 'miles':
            return self.length * 63360
        elif self.unit == 'kilometers':
            return self.length * 39370.1
        elif self.unit == 'meters':
            return self.length * 39.3701
        elif self.unit == 'centimeters':
            return self.length * 0.393701
        elif self.unit == 'millimeters':
            return self.length * 0.0393701

    def feet(self):
        if self.unit == 'feet':
            return self.length
        elif self.unit == 'inches':
            return self.length / 12
        elif self.unit == 'yards':
            return self.length * 3
        elif self.unit == 'miles':
            return self.length * 5280
        elif self.unit == 'kilometers':
            return self.length * 3280.84
        elif self.unit == 'meters':
            return self.length * 3.28084
        elif self.unit == 'centimeters':
            return self.length * 0.0328084
        elif self.unit == 'millimeters':
            return self.length * 0.00328084

    def yards(self):
        if self.unit == 'yards':
            return self.length
        elif self.unit == 'inches':
            return self.length / 36
        elif self.unit == 'feet':
            return self.length / 3
        elif self.unit == 'miles':
            return self.length * 1760
        elif self.unit == 'kilometers':
            return self.length * 1093.61
        elif self.unit == 'meters':
            return self.length * 1.09361
        elif self.unit == 'centimeters':
            return self.length * 0.0109361
        elif self.unit == 'millimeters':
            return self.length * 0.00109361

    def miles(self):
        if self.unit == 'miles':
            return self.length
        elif self.unit == 'inches':
            return self.length / 63360
        elif self.unit == 'feet':
            return self.length / 5280
        elif self.unit == 'yards':
            return self.length / 1760
        elif self.unit == 'kilometers':
            return self.length / 1.609
        elif self.unit == 'meters':
            return self.length / 1609
        elif self.unit == 'centimeters':
            return self.length / 160900
        elif self.unit == 'millimeters':
            return self.length / 1609344

    def kilometers(self):
        if self.unit == 'kilometers':
            return self.length
        elif self.unit == 'inches':
            return self.length / 39370
        elif self.unit == 'feet':
            return self.length / 3281
        elif self.unit == 'yards':
            return self.length / 1094
        elif self.unit == 'miles':
            return self.length * 1.60934
        elif self.unit == 'meters':
            return self.length * 0.001
        elif self.unit == 'centimeters':
            return self.length / 100000
        elif self.unit == 'millimeters':
            return self.length / 1000000

    def meters(self):
        if self.unit == 'meters':
            return self.length
        elif self.unit == 'inches':
            return self.length / 39.37
        elif self.unit == 'feet':
            return self.length * 0.3048
        elif self.unit == 'yards':
            return self.length * 0.9144
        elif self.unit == 'miles':
            return self.length * 1609.34
        elif self.unit == 'kilometers':
            return self.length * 1000
        elif self.unit == 'centimeters':
            return self.length * 0.01
        elif self.unit == 'millimeters':
            return self.length / 1000

    def centimeters(self):
        if self.unit == 'centimeters':
            return self.length
        elif self.unit == 'inches':
            return self.length * 2.54
        elif self.unit == 'feet':
            return self.length * 30.48
        elif self.unit == 'yards':
            return self.length * 91.44
        elif self.unit == 'miles':
            return self.length * 160934
        elif self.unit == 'kilometers':
            return self.length * 100000
        elif self.unit == 'meters':
            return self.length * 100
        elif self.unit == 'millimeters':
            return self.length / 10

    def millimeters(self):
        if self.unit == 'millimeters':
            return self.length
        elif self.unit == 'inches':
            return self.length * 25.4
        elif self.unit == 'feet':
            return self.length * 304.8
        elif self.unit == 'yards':
            return self.length * 914.4
        elif self.unit == 'miles':
            return self.length * 1609344
        elif self.unit == 'kilometers':
            return self.length * 1000000
        elif self.unit == 'meters':
            return self.length * 1000
        elif self.unit == 'centimeters':
            return self.length * 10
