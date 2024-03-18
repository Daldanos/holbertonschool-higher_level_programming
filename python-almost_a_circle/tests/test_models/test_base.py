import unittest
from base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        # Test initialization with default value
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        # Test initialization with custom value
        obj2 = Base(10)
        self.assertEqual(obj2.id, 10)

    def test_to_json_string(self):
        # Test to_json_string method with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test to_json_string method with list of dictionaries
        list_dicts = [{'id': 1, 'name': 'apple'}, {'id': 2, 'name': 'banana'}]
        expected_json = '[{"id": 1, "name": "apple"}, {"id": 2, "name": "banana"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_from_json_string(self):
        # Test from_json_string method with empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test from_json_string method with JSON string
        json_string = '[{"id": 1, "name": "apple"}, {"id": 2, "name": "banana"}]'
        expected_list = [{'id': 1, 'name': 'apple'}, {'id': 2, 'name': 'banana'}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_create(self):
        # Test create method with dictionary
        dictionary = {'id': 1, 'name': 'apple'}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, 'apple')

    def test_save_to_file(self):
        # Test save_to_file method with empty list
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

        # Test save_to_file method with list of instances
        class TestClass(Base):
            pass

        obj1 = TestClass(1)
        obj2 = TestClass(2)
        Base.save_to_file([obj1, obj2])
        with open('Base.json', 'r') as file:
            content = file.read()
            expected_content = '[{"id": 1}, {"id": 2}]'
            self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
