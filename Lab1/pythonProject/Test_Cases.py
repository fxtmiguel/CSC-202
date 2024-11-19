import unittest
import main


class TestCases(unittest.TestCase):
    def test_product(self):
        item = main.Product("Shirt", 1, 500)
        item_1 = item.get_price(5)
        self.assertEqual(item_1, 2500)

    def test_product_1(self):
        item = main.Product("Wrist Watch", 2, 1200)
        item_2 = item.get_price(15)
        self.assertEqual(item_2, 16200)

    def test_product_2(self):
        item = main.Product("Textbook", 2, 800)
        item_3 = item.get_price(100)
        self.assertEqual(item_3, 64000)

    def test_product_3(self):
        item = main.Product("History Book", 2, 500)
        item_4 = item.get_price(100)
        self.assertEqual(item_4, 40000)

    def test_make_purchase(self):
        item = main.Product("Memory Card", 10, 1400)
        item_5 = item.make_purchase(100)
        self.assertEqual(item_5, 90)

    def test_unit(self):
        unit = main.Converter(6, "inches")
        unit_2 = unit.feet()
        self.assertEqual(unit_2, .5)

    def test_unit2(self):
        unit = main.Converter(9, "feet")
        unit_2 = unit.yards()
        self.assertEqual(unit_2, 3)

    def test_unit3(self):
        unit = main.Converter(2000, "yards")
        unit_2 = unit.miles()
        self.assertEqual(unit_2, 1.1363636363636365)

    def test_unit4(self):
        unit = main.Converter(5000, "miles")
        unit_2 = unit.kilometers()
        self.assertEqual(unit_2, 8046.7)

    def test_unit5(self):
        unit = main.Converter(100, "kilometers")
        unit_2 = unit.meters()
        self.assertEqual(unit_2, 100000)

    def test_unit6(self):
        unit = main.Converter(100, "meters")
        unit_2 = unit.centimeters()
        self.assertEqual(unit_2, 10000)

    def test_unit7(self):
        unit = main.Converter(35, "centimeters")
        unit_2 = unit.millimeters()
        self.assertEqual(unit_2, 350)




    if __name__ == '__main__':
        unittest.main()
