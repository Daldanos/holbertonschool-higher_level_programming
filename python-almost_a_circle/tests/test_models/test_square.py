import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        # Test initialization with default values
        sq1 = Square()
        self.assertEqual(sq1.size, 0)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)
        self.assertEqual(sq1.id, 1)

        # Test initialization with custom values
        sq2 = Square(5, 2, 3, 10)
        self.assertEqual(sq2.size, 5)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 3)
        self.assertEqual(sq2.id, 10)

    def test_area(self):
        # Test area calculation
        sq1 = Square(5)
        self.assertEqual(sq1.area(), 25)

        sq2 = Square(10)
        self.assertEqual(sq2.area(), 100)

    def test_str(self):
        # Test string representation
        sq1 = Square(5, 2, 3, 10)
        self.assertEqual(str(sq1), "[Square] (10) 2/3 - 5")

    def test_update(self):
        # Test update method
        sq1 = Square(5, 2, 3, 10)
        sq1.update(20, 7, 8, 15)
        self.assertEqual(str(sq1), "[Square] (20) 7/8 - 7")

    def test_to_dictionary(self):
        # Test to_dictionary method
        sq1 = Square(5, 2, 3, 10)
        self.assertEqual(sq1.to_dictionary(), {'id': 10, 'size': 5, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()
