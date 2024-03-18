import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test initialization with default values
        rect1 = Rectangle()
        self.assertEqual(rect1.width, 0)
        self.assertEqual(rect1.height, 0)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, 1)

        # Test initialization with custom values
        rect2 = Rectangle(5, 4, 2, 3, 10)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 3)
        self.assertEqual(rect2.id, 10)

    def test_area(self):
        # Test area calculation
        rect1 = Rectangle(5, 4)
        self.assertEqual(rect1.area(), 20)

        rect2 = Rectangle(10, 6)
        self.assertEqual(rect2.area(), 60)

    def test_str(self):
        # Test string representation
        rect1 = Rectangle(5, 4, 2, 3, 10)
        self.assertEqual(str(rect1), "[Rectangle] (10) 2/3 - 5/4")

    def test_update(self):
        # Test update method
        rect1 = Rectangle(5, 4, 2, 3, 10)
        rect1.update(20, 7, 8, 6, 5)
        self.assertEqual(str(rect1), "[Rectangle] (20) 7/8 - 6/5")

    def test_to_dictionary(self):
        # Test to_dictionary method
        rect1 = Rectangle(5, 4, 2, 3, 10)
        self.assertEqual(rect1.to_dictionary(), {'id': 10, 'width': 5, 'height': 4, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()
