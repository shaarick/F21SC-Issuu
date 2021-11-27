import unittest
from convert import Convert


class ConversionTest(unittest.TestCase):

    def setUp(self) -> None:
        "Setup a converter to be used by other classes"
        self.convert = Convert()

    def test_country_to_continent_one(self):
        """Test country code to continent conversion with valid input"""
        self.assertEqual(self.convert.to_continent_code('AF'), 'AS', 'Should be AS')

    def test_country_to_continent_two(self):
        """Test country code to continent conversion with invalid input"""
        self.assertRaises(KeyError, self.convert.to_continent_code, 'abcd')

    def test_country_to_continent_three(self):
        """Test country code to continent conversion with valid but unrecognized input"""
        self.assertRaises(KeyError, self.convert.to_continent_code, 'xx')

    def test_continent_name_one(self):
        """Test continent code to full name with valid input"""
        self.assertEqual(self.convert.to_continent_name('EU'), 'Europe', 'Should be Europe')

    def test_continent_name_two(self):
        """Test continent code to full name with invalid input"""
        self.assertRaises(KeyError, self.convert.to_continent_name, 'XYZ')

    def test_continent_name_three(self):
        """Test continent code to full name with valid but unrecognized input"""
        self.assertRaises(KeyError, self.convert.to_continent_name, 'XX')


if __name__ == '__main__':
    unittest.main()
